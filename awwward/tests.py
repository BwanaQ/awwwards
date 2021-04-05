from django.test import TestCase
from .models import Rating, Project
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='dorothy')
        self.user.save()

        self.profile_test = Profile(id=1, phone_number='0722222222', image='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


class ProjectTestCase(TestCase):
    def setUp(self):
        pass


class RatingTestCase(TestCase):
    def setUp(self):
        pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default_fiis58.jpg',
                              upload_to='awwwards_profile_pics')
    phone_number = PhoneField(
        blank=True, help_text='Contact phone number', E164_only=False)
