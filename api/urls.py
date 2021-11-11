"""
    API ENDPOINTS
"""
from django.urls import path
from .views import  register_user, test, save_task, task_detail

urlpatterns = [
    path('hi', save_task, name='hello'),
    path('todos', save_task, name='task'),
    path('todos/<int:pk>',task_detail, name='task_detail'),
    path('signup', register_user, name='register'),
]
