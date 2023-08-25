from django.shortcuts import render
from rest_framework import generics
from taskapp.models import Task
from .serializers import TaskSerializer

# Create your views here.
class AllTasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer