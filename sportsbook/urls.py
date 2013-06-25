from django.contrib import admin
from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('news.urls')),
    url(r'^sportsbook/', include('book.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
