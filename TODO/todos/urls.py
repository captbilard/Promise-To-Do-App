from django.urls import path, include
from .views import AddTodoView

urlpatterns = [
    path('', AddTodoView.as_view(), name='add-todo'),
]
