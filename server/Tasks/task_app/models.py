from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Model representing a task with various attributes.
    """
    STATUS_CHOICES = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    )
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Progress')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    due_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

 #Create Meta class inside the Task model
class Meta:
        indexes = [models.Index(fields=['title']),]
        permissions = [
        ("change_task", "Can change task"),
    ]
