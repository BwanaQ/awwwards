from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default_fiis58.jpg',
                              upload_to='awwwards_profile_pics')
    phone_number = PhoneField(
        blank=True, help_text='Contact phone number', E164_only=False)

    def __str__(self):
        return f"{self.user.username} Profile"
