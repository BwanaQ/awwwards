from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    image = models.ImageField(upload_to='awwwards/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    """def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
"""


class Rating(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commentor')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    """def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
"""
