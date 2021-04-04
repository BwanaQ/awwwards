from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils.timezone import utc
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Project, Rating
from django.urls import reverse
from .forms import RatingCreateForm


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    ordering = ['-timestamp']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        return context


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        rating_form = RatingCreateForm()
        context['rating_form'] = rating_form

        return context


class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingCreateForm

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(CreateArticle, self).form_valid(form)
