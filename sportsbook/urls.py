from django.contrib import admin
from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('news.urls')),
    url(r'^sportsbook/', include('book.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
