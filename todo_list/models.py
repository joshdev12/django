from email.policy import default
from turtle import update
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    time = models.DateTimeField()
    status = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_add_now=True)
    # update_at = models.DateTimeField(auto_add=True)

    def __str__(self) -> str:
        return self.title

