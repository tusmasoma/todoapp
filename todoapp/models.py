from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200) #タイトル
    description = models.TextField(blank=True, null=True) #詳細
    created_at = models.DateTimeField(auto_now_add=True) #作成日
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title