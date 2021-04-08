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
from django.urls import reverse_lazy
from .forms import RatingCreateForm
from django.shortcuts import get_object_or_404


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    ordering = ['-timestamp']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Project.objects.filter(title__icontains=query)
        else:
            return Project.objects.all()


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


class ProjectDetailView(DetailView):
    model = Project


class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    form_class = RatingCreateForm

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Project` instance exists
        before going any further.
        """
        self.project = get_object_or_404(Project, pk=kwargs['pk'])

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.project = self.project

        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('awwward-detail', kwargs={'pk': pk})


class RatingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rating
    form_class = RatingCreateForm

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super().form_valid(form)

    def test_func(self):
        rating = self.get_object()
        if self.request.user == rating.creator:
            return True
        return False

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('awwward-home')


class RatingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rating
    success_url = '/'

    def test_func(self):
        rating = self.get_object()
        if self.request.user == rating.creator:
            return True
        return False
