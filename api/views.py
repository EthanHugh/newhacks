from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from api import serializers
from api import models

# Create your views here.

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.all()


class Course212ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.filter(course="ECE212")
    

class Course241ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.filter(course="ECE241")

    
class Course244ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.filter(course="ECE244")

    
class Course290ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.filter(course="MAT290")


class Course291ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = models.Assignment.objects.filter(course="MAT291")