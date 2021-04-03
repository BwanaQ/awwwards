from django.forms import ModelForm, HiddenInput
from django.views.generic.edit import CreateView
from .models import Rating, Project
from captcha.fields import CaptchaField


class RatingCreateForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Rating
        exclude = ['creator', 'project', 'timestamp']
