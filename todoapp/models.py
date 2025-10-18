from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed')]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=255)
    descrription=models.TextField(blank=True)
    task_status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_on=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
