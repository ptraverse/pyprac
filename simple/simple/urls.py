from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscoveradurlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple.views.home', name='home'),
    # url(r'^simple/', include('simple.foo.urls')),
urlpatterns = patterns ( '',
url(r'^user/(.+)/viewingad/(.+)/','simple.simpletest.views.view_ad'),
url(r'^newad/(.+)/(.+)/$','simple.simpletest.views.create_ad'),
url(r'^newuser/(.+)/$','simple.simpletest.views.create_user'),
url(r'^home/','simple.simpletest.views.home'),
	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
