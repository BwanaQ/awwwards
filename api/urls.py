from django.urls import path
from .views import ProjectAPIView, RatingAPIView, UserAPIView
urlpatterns = [
    path('projects/', ProjectAPIView.as_view()),
    path('ratings/', RatingAPIView.as_view()),
    path('users/', UserAPIView.as_view()),
]
