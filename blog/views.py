from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PersonSerializer
from blog.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
