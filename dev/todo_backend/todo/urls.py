from rest_framework import routers

from todo.views import TodoViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
router.register('todos-lists', TodoListViewSet)
