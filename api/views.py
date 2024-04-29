from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

@api_view(['GET'])
def getUsers(request):
    instance = UserList.objects.all()
    serializer = UserListSerializer(instance, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def  getUser(request, pk=None):
    try:
        if pk:
            instance = UserList.objects.get(pk=pk)
        else:
            instance = UserList.objects.all()
        serializer = UserListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except UserList.DoesNotExist:
        return Response({"ERROR": "The provided user does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(["POST"])
def createUser(request):
    serializer = UserListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PATCH", "PUT"])
def updateUser(request, pk=None):
    try:
        instance = UserList.objects.get(pk=pk)
        serializer = UserListSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    except UserList.DoesNotExist:
        return Response({"ERROR": "The provided user does not exist!"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def deleteUser(request, pk=None):
    try:
        instance = UserList.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except UserList.DoesNotExist:
        return Response({"ERROR": "The provided user does not exist!"}, status=status.HTTP_404_NOT_FOUND)