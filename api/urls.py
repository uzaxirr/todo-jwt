"""
    API ENDPOINTS
"""
from django.urls import path
from .views import HelloView, register_user

urlpatterns = [
    path('hi', HelloView.as_view(), name='hello'),
    path('register', register_user, name='register'),
]
