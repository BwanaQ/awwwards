from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView
urlpatterns = [
    path('', ProjectListView.as_view(), name='awwward-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='awwward-detail'),

]
