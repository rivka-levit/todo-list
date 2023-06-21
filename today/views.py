from django.shortcuts import render, redirect
from django.views.generic import View


class TodayView(View):
    def get(self, request):
        return render(request, 'today/today.html', {'title': 'TODO LIST - Today'})


def undo_task(request):
    print('undo')
    return redirect('today:today_tasks')
