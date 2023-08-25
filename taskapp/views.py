from django.shortcuts import render
from django.core.cache import cache

from .models import Task

# Create your views here.

def task_list(request):
    cached_tasks = cache.get('cached_tasks')

    if cached_tasks is None:
        tasks = Task.objects.all()
        cache.set('cached_tasks', Task, timeout=3600)

    else:
        tasks = cached_tasks

    return render(request, 'task-list.html', {'tasks': tasks})

