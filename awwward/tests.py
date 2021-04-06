from django.test import TestCase
from .models import Rating, Project
from django.contrib.auth.models import User
from users.models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='dorothy')
        self.user.save()

        self.profile_test = Profile(id=1, phone_number='0722222222', image='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))


class ProjectTestCase(TestCase):
    def setUp(self):
        pass


class RatingTestCase(TestCase):
    def setUp(self):
        pass
