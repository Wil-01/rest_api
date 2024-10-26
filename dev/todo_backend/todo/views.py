from django.shortcuts import render
from rest_framework import viewsets

from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer

class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_fields = ['due_date', 'favourite', 'completed']
    search_fields = ['tittle']
    
class TodoListViewSet(viewsets.ModelViewSet):
    
    queryset = TodoList.objects.all()
    serializers_class = TodoListSerializer
