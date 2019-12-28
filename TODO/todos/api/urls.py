from rest_framework import routers
from .views import TodoViewSet
from django.urls import path


router =  routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todos')

urlpatterns = router.urls