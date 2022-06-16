from django.urls import path, include
from .views import SignupView, HomeView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", HomeView),
    path("signup/", SignupView)
]
