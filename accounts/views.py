from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import SignupForm


class SignupView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = SignupForm

    def get_success_url(self):
        return reverse("myprofile")


class MyProfileView(DetailView):
    template_name = "my_profile.html"
    model = User

