from django.urls import path
from .views import TodayView, undo_task, mark_done, delete_task

app_name = 'today'

urlpatterns = [
    path('', TodayView.as_view(), name='today_tasks'),
    path('done/<int:task_id>/', mark_done, name='done'),
    path('delete/<int:task_id>', delete_task, name='delete_task'),
    path('undo/<int:task_id>/', undo_task, name='undo'),
]
