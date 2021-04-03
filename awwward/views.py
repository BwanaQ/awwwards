from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils.timezone import utc
from django.views.generic import ListView
from django.views.generic.list import MultipleObjectMixin
from .models import Project, Rating


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
