from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.timezone import utc
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['image', 'title', 'description', 'link']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['image', 'title', 'description', 'link']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.creator:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.creator:
            return True
        return False


class ProjectDetailView(LoginRequiredMixin, DetailView):
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
        return reverse('awwward-detail', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.project = self.object.project.pk

        return super(CreateRating, self).form_valid(form)
