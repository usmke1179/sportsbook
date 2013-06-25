from django.views.generic import TemplateView
# from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "registration/profile.html"
