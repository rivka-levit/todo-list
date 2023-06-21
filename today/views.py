from django.shortcuts import render, redirect
from django.views.generic import View
from .models import TaskModel


class TodayView(View):
    def get(self, request):
        tasks = TaskModel.objects.filter(is_done=False)
        completed = TaskModel.objects.filter(is_done=True)
        return render(request, 'today/today.html', {
            'title': 'TODO LIST - Today',
            'tasks': tasks,
            'completed': completed
        })


def mark_done(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return redirect(request.META['HTTP_REFERER'])


def undo_task(request, task_id):
    print('undo')
    return redirect('today:today_tasks')
