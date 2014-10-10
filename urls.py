from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import SongView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^song/$', SongView.as_view(), name='song'),
    url(r'^$', SongView.as_view(), name='home'),
)
