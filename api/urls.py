from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProjectAPIView, RatingAPIView, UserAPIView, ProjectDetail, RatingDetail, UserDetail
urlpatterns = [
    path('projects/', ProjectAPIView.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('ratings/', RatingAPIView.as_view()),
    path('ratings/<int:pk>/', RatingDetail.as_view()),
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
