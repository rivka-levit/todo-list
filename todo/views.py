from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Task
from .forms import EditTaskForm
from django.contrib import messages


class TodayView(View):
    def get(self, request):
        tasks = Task.objects.filter(is_done=False)
        completed = Task.objects.filter(is_done=True)
        return render(request, 'todo/today.html', {
            'title': 'TODO LIST - Today',
            'tasks': tasks,
            'completed': completed
        })

    def post(self, request):
        task_name = request.POST['add_task']
        new_task = Task(name=task_name)
        new_task.save()
        return redirect(request.META['HTTP_REFERER'])


class EditView(View):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        form = EditTaskForm(instance=task)
        return render(request, 'todo/edit.html', {
            'task': task,
            'form': form
        })

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:today_tasks')
        messages.error(request, 'Invalid input!')
        return redirect(request.META['HTTP_REFERER'])


def mark_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect(request.META['HTTP_REFERER'])


def undo_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = False
    task.save()
    return redirect('todo:today_tasks')
