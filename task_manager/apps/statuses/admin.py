# task_manager/apps/statuses/admin.py
from django.contrib import admin

from .models import Status

admin.site.register(Status)
