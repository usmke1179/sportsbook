from django.conf.urls import patterns, url
from .views import BaseballView, BasketballView, FootballView  # , HockeyView

urlpatterns = patterns(
    '',
    url(r'^mlb/$', BaseballView.as_view(), name='baseball'),
    url(r'^nba/$', BasketballView.as_view(), name='basketball'),
    url(r'^nfl/$', FootballView.as_view(), name='football'),
    # url(r'^nhl$', HockeyView.as_view(), name='hockey'),
)
