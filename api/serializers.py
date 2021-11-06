from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from api import models

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Assignment
        fields = '__all__'