from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'is_done']


admin.site.register(Task, TaskAdmin)
