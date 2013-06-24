from django.conf.urls import patterns, url
from .views import SignupView, MyProfileView

urlpatterns = patterns(
    '',
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^myprofile/$', MyProfileView.as_view(), name='myprofile'),
)
