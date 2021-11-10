"""
    API VIEWS
"""
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class HelloView(APIView):
    """ Testing View Class """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

@api_view(['POST'])
def register_user(request):
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        refresh = RefreshToken.for_user(User)
        return Response({'status': status.HTTP_201_CREATED, 'data': serialized_data.data, 'access': str(refresh.access_token), 'refresh': str(refresh)}, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    