from django.urls import path
from .views import SubscriptionListCreateViews

urlpatterns = [
    path('subcriptions/', SubscriptionListCreateViews.as_view(),name='subscriptions')
]