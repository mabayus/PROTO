from django.conf.urls import patterns, include, url

from django.contrib import admin
from login.views import acceuil
from inscription.views import incription
from description_probleme.views import discribe_probleme
from upload_algo.views import upload_file
from description_probleme.jqueryFileTree import dirlist
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proto1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', acceuil),
    url(r'^inscription/', incription),
    url(r'^upload_file/', upload_file),
    url(r'^discribe_probleme/', discribe_probleme),
    url(r'^arboraissance/', dirlist),
)
