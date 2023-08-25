from django.urls import path
from api.views import AllTasks, TaskInfo

urlpatterns = [
    path('taskapp/', AllTasks.as_view(), name='task-list'),
    path('taskapp/<int:pk>/', TaskInfo.as_view(), name='task-info')
]