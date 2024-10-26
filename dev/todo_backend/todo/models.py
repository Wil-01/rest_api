from django.db import models


class Todo(models.Model):
    
    tittle = models.CharField(max_length=250)
    due_date = models.DateField()
    completed = models.BooleanField()
    favourite = models.BooleanField()
    
    list = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)
    
    
class TodoList(models.Model):
    
    name = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
    