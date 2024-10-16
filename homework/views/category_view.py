from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from homework.models.category import Category
from homework.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    @action(detail=True, methods=['get'], url_path='count-tasks')
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = category.tasks.count()  # assuming you have a related_name='tasks' in the Task model
        return Response({'category_id': pk, 'task_count': task_count})

