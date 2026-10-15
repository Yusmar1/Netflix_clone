from django.urls import path
from .views import VideoListCreateViews

urlpatterns = [
    path('video/', VideoListCreateViews.as_view(),name='video')
]