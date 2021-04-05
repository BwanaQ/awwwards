from django.urls import path
from . import views
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,

    RatingCreateView
)
urlpatterns = [
    path('', ProjectListView.as_view(), name='awwward-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='awwward-detail'),
    path('awwward/new/', ProjectCreateView.as_view(), name='awwward-create'),
    path('awwward/<int:pk>/update/',
         ProjectUpdateView.as_view(), name='awwward-update'),
    path('awwward/<int:pk>/delete/',
         ProjectDeleteView.as_view(), name='awwward-delete'),
    path('awwward/<int:pk>/comment/',
         RatingCreateView.as_view(), name='awwward-delete'),


]
