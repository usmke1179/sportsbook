from django.conf.urls import patterns, url
from .views import BaseballView

urlpatterns = patterns(
    '',
    url(r'^mlb$', BaseballView.as_view(), name='baseball'),
)
