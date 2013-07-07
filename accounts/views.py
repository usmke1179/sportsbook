from django_tables2 import SingleTableView
# from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin
from . import tables
from book import models


class ProfileView(LoginRequiredMixin, SingleTableView):
    template_name = "history.html"
    table_pagination = False
    table_class = tables.BaseballLinesTable

    def get_queryset(self):
        userbets = models.Bet.objects.filter(user_id=self.request.user.id)
        return userbets
