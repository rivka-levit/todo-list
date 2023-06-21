from django.urls import path
from .views import TodayView

app_name = 'today'

urlpatterns = [
    path('', TodayView.as_view(), name='today_tasks'),
]
