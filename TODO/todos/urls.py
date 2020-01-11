from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', AddTodoView.as_view(), name='add-todo'),
    path('done/<int:todo_id>', completed, name='completed'),
    path('delete-completed/', deleteCompleted, name='delete-completed'),
    path('delete-all/', deleteAll, name='delete-all'),
    
]
