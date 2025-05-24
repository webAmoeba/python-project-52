from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, required=True, label=_("First name")
    )
    last_name = forms.CharField(
        max_length=150, required=True, label=_("Last name")
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )

    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.exclude(pk=self.instance.pk)
        if qs.filter(username=username).exists():
            raise forms.ValidationError(
                _("User with this username already exists.")
            )
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label=_("First name"))
    last_name = forms.CharField(required=True, label=_("Last name"))
    username = forms.CharField(required=True, label=_("Username"))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]
