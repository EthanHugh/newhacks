from django.db import models

import uuid

# Create your models here.

class Assignment(models.Model):
    """Profile information"""
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=30)
    assignment_name = models.CharField(max_length=30)
    date = models.IntegerField()
    month = models.IntegerField()
    weight = models.FloatField()
    content = models.TextField()
    submission_link = models.TextField()
    reference_link = models.TextField()

    def __str__(self):
        """Return the model as a string"""
        return str(self.assignment_name)

