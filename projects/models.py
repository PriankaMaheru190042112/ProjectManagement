from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Todo', 'Todo'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Todo')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
