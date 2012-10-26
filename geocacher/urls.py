from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
                       url(r'^$', 'geocacher.caches.views.home'),
                       url(r'^register', 'geocacher.account.views.register'),
                       url(r'^user/(?P<name>\w+)/$', 'geocacher.account.views.user_profile'),
                       url(r'^cache/(?P<id>\d+)/$', 'geocacher.caches.views.view_cache'),
                       url(r'^caches/', 'geocacher.caches.views.cache_list'),
                       url(r'^cache_ajax', 'geocacher.caches.views.cache_ajax'),
                       url(r'^create', 'geocacher.caches.views.add_cache'),
                       url(r'^login', 'geocacher.account.views.login_user'),
                       url(r'^logout', 'geocacher.account.views.log_out'),
                       url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),

    # url(r'^$', 'geocacher.views.home', name='home'),
    # url(r'^geocacher/', include('geocacher.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
