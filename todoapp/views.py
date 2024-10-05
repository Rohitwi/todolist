from django.shortcuts import render
from .models import Task
# Create your views here.


def showlist(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/showlist.html', {'tasks': tasks})

def add_task(request):
    title = request.POST.get('title')
    if title:
        Task.objects.create(title=title)
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks':tasks})

def remove_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

