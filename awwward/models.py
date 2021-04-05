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

    def get_absolute_url(self):
        return reverse('awwward-detail', kwargs={'pk': self.pk})


class Rating(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')

    )
    design = models.IntegerField(choices=RATING)
    usability = models.IntegerField(choices=RATING)
    content = models.IntegerField(choices=RATING)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rater')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='ratings')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.creator.username} rating for {self.project.title}"

    def get_absolute_url(self):
        return reverse('awwward-detail', kwargs={'pk': self.pk})

    def get_average_percentage(self):
        avg = ((self.design+self.usability+self.content)/3)*10
        avg_pc = int(avg)
        return avg_pc
