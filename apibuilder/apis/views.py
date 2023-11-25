from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApisSerializer

from .models import Student
# Create your views here.


class ApisViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Student.objects.all()
 
    # specify serializer to be used
    serializer_class = ApisSerializer