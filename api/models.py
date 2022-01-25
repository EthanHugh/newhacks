from django.db import models

import uuid

# Create your models here.

class Assignment(models.Model):
    """Profile information"""
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=30)
    assignment_name = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        """Return the model as a string"""
        return str(self.course) + " - " + str(self.assignment_name)
    
class Old_Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=30)
    assignment_name = models.CharField(max_length=30)
    date = models.DateField()
    
    def __str__(self):
        """Return the model as a string"""
        return str(self.course) + " - " + str(self.assignment_name)