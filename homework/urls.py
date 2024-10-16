from django.urls import path
from rest_framework import routers

from homework.views.category_view import CategoryViewSet
from homework.views.subtask_view import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
urlpatterns = router.urls

# Add your custom URLs to the existing `urlpatterns` list
urlpatterns += [
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]