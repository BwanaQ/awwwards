from rest_framework import serializers
from awwward.models import Project, Rating
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('image', 'title', 'description',
                  'link', 'creator', 'timestamp')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content',
                  'creator', 'creator', 'project', 'timestamp')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
