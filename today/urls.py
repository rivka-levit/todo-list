from django.urls import path
from .views import TodayView, undo_task

app_name = 'today'

urlpatterns = [
    path('', TodayView.as_view(), name='today_tasks'),
    path('undo/', undo_task, name='undo'),
]
