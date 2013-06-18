from django.conf.urls import patterns, url
from .views import NewsView

urlpatterns = patterns(
    '',
    url(r'^$', NewsView.as_view(), name='news'),
)
