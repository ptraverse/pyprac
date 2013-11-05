from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^post/(.+)/','gim3.gimmeapp.views.view_post'),
	url(r'^hello_world/(.+)/','gim3.gimmeapp.views.hello_world'),
	url(r'^allposts/','gim3.gimmeapp.views.view_all_posts'),
    # Examples:
    # url(r'^$', 'gim3.views.home', name='home'),
    # url(r'^gim3/', include('gim3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^create-post/','gim3.gimmeapp.views.create_post'),
	url(r'^/preforms/create-post/','gim3.gimmeapp.views.create_post'),
	url(r'^preform/','gim3.gimmeapp.views.preform'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
