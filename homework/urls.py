from django.urls import path

from .serializers.task_serializer import TaskCreateSerializer, TaskDetailSerializer
from .views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView, TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('task/', TaskListCreateAPIView.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]
