from django.urls import path

from .views import index, TodoDetailView

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>', TodoDetailView.as_view(), name='edit'),
    path('delete/<int:pk>', TodoDetailView.as_view(), name='delete')

]
