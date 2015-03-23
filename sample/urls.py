from django.conf.urls import patterns, include, url
from django.contrib import admin

from contact import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name="contact"),
)
