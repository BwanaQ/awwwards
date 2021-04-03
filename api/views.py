from django.shortcuts import render
from api import serializers
# Create your views here.
from rest_framework import generics
from awwward.models import Project, Rating
from .serializers import ProjectSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class RatingAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDetail(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
