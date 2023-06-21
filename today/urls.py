from django.urls import path
from .views import TodayView, undo_task, mark_done

app_name = 'today'

urlpatterns = [
    path('', TodayView.as_view(), name='today_tasks'),
    path('done/<int:task_id>/', mark_done, name='done'),
    path('undo/<int:task_id>/', undo_task, name='undo'),
]
