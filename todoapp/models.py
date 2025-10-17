from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed')]

    title=models.CharField(max_length=255)
    descrription=models.TextField(blank=True)
    task_status=models.CharField(max_length=20,choices=STATUS_CHOICES)
    created_on=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
