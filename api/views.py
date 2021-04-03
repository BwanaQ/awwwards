from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from awwward.models import Project, Rating
from .serializers import ProjectSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RatingAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
