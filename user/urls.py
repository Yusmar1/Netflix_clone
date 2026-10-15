from django.urls import path
from .views import UserListCreateView, GetSingleUser

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="users"), 
    path("get-single-user/<int:param>/", GetSingleUser.as_view(), name="get-single-user")
]