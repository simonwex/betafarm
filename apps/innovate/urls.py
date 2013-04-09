from django.conf.urls.defaults import patterns, url
from django.views.generic.base import TemplateView

from csp.decorators import csp_exempt


urlpatterns = patterns('',
    url(r'^/?$', 'innovate.views.splash', name='innovate_splash'),
    url(r'^about/$', 'innovate.views.about', name='innovate_about'),
    url(r'^hatchery/$', 'innovate.views.hatchery', name='innovate_hatchery'),
    url(r'^search/$',
        csp_exempt(TemplateView.as_view(template_name='innovate/search.html')),
        name='innovate_search'),
)
