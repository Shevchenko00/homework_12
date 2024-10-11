from rest_framework.pagination import PageNumberPagination

from rest_framework import generics
from .models.task import SubTask, Task  # Предполагаем, что модель SubTask уже определена
from .serializers.task_serializer import SubTaskCreateSerializer, SubTaskDetailSerializer, TaskCreateSerializer, \
    TaskDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    pagination_class = PageNumberPagination
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'dedline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskDetailSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'dedline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
