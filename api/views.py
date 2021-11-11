"""
    API VIEWS
"""
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, TaskSerializer
from .models import TaskModel
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

# class HelloView(APIView):
#     """ Testing View Class """
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

@api_view(['POST'])
def register_user(request):
    """View To Register a new User"""
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        refresh = RefreshToken.for_user(User)
        return Response({'status': status.HTTP_201_CREATED, 'data': serialized_data.data, 'access': str(refresh.access_token), 'refresh': str(refresh)}, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    """Testing View"""
    js_res = {
        'User ID': request.user.id
    }
    return Response(js_res)

# make view authorized only

@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def save_task(request):
    """View to save a new task"""
    if request.method == 'GET':
        required_data = TaskModel.objects.filter(created_by= request.user.id)
        serializer = TaskSerializer(required_data, many=True)
        return Response({'status': status.HTTP_200_OK, 'data': serializer.data},status=status.HTTP_200_OK)
    elif request.method == 'POST':
        input_data = request.data
        input_data['created_by'] = request.user.id
        serialized_data = TaskSerializer(data=input_data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': status.HTTP_201_CREATED, 'data': serialized_data.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST ,'Error':serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'status': 'Method not allowed'})

@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """View to get, update or delete a task"""
    try:
        task = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'Error': 'Task Not Found or Does Not Exist'})

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response({'status': status.HTTP_200_OK, 'data': serializer.data})
    elif request.method == 'PUT':
        input_data = request.data
        input_data['created_by'] = request.user.id
        serializer = TaskSerializer(task, data=input_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response({'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'status': 'Method not allowed'})
        