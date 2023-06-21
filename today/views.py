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

    def post(self, request):
        task_name = request.POST['add_task']
        new_task = TaskModel(name=task_name)
        new_task.save()
        return redirect(request.META['HTTP_REFERER'])


def mark_done(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect(request.META['HTTP_REFERER'])


def undo_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_done = False
    task.save()
    return redirect('today:today_tasks')
