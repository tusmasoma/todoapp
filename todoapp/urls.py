from django.urls import path,include
from rest_framework import routers
from .views import TaskViewSet

app_name='todoapp'

router = routers.DefaultRouter()
router.register(r'task',TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
