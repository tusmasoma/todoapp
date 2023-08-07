from rest_framework import routers, serializers, viewsets
from .models import Task
# Create your views here.


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'