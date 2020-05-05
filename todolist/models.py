from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    due_by = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def task_done(self):
        self.done = True
