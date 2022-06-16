from django.urls import path
from .views import LoginView, SignupView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='home.html'), name="home"),
    path("login/", LoginView, name="login"),
    path("signup/", SignupView, name="signup"),
    path("logout/", LogoutView, name="logout")
]
