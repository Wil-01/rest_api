from django.test import TestCase

from todo.models import Todo, TodoList

from datetime import datetime

class TodoTestCase(TestCase):
    
    DUMMY_TODO_TITTLE = 'Test Element'
    
    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name = 'Test Todo List'
        self.todoList.save()
        
        self.todoListTestElement = Todo()
        self.todoListTestElement.tittle = self.DUMMY_TODO_TITTLE
        self.todoListTestElement.due_date = datetime.today()
        self.todoListTestElement.completed = True
        self.todoListTestElement.favourite = False
        self.todoListTestElement.list = self.todoList
        self.todoListTestElement.save()        
    
    def test_create_todo(self):
        
        nbr_of_todos_before_add = Todo.objects.count()
        
        new_todo = Todo()
        new_todo.tittle = "Acheter de l'eau"
        new_todo.due_date = datetime.today()
        new_todo.favourite = True
        new_todo.completed = False
        new_todo.list = self.todoList
        
        
        new_todo.save()
        
        nbr_of_todos_after_add = Todo.objects.count() 
        
        self.assertTrue(nbr_of_todos_after_add == nbr_of_todos_before_add + 1)
         
    def test_updat_todo(self):
        
        self.assertEqual(self.todoListTestElement.tittle, self.DUMMY_TODO_TITTLE)
        
        self.todoListTestElement.tittle = 'Changed'
        self.todoListTestElement.save()
        
        tempElement = Todo.objects.get(pk = self.todoListTestElement.pk)
        
        self.assertEqual(tempElement.tittle, 'Changed')
        
    def test_delete_todo(self):
        
        nbr_of_tood_before_delete = Todo.objects.count()
        
        self.todoListTestElement.delete()
        
        nbr_of_tood_after_delete = Todo.objects.count()
        
        self.assertTrue(nbr_of_tood_after_delete == nbr_of_tood_before_delete -1)        