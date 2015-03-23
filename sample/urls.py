from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home
from contact import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name="home"),
    url(r'^contact/$', views.contact, name="contact"),
)
