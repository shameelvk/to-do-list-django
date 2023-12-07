from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)