from django.contrib import admin

from todo.models import Todo, TodoList

class TodoInline(admin.TabularInline):
    
    model = Todo
    extra = 1

@admin.register( TodoList)
class TodoListAdmin(admin.ModelAdmin):
    
    list_display = ('name',)
    inlines = (TodoInline, )


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    
    list_display = ('tittle', 'due_date', 'completed','favourite')
    list_filter = ('due_date', 'completed','favourite')
    search_fields = ('tittle',)