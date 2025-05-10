from django.urls import path

from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
]