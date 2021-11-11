import uuid
from django.db import models

# Create your models here.

#TODO task model
class TaskModel(models.Model):
    """Model For Task"""
    # id = models.IntegerField(primary_key=True)
    created_by = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
