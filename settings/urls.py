from django.conf.urls import patterns, include, url
from django.contrib import admin
import homepage.views.errors

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lexicity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # the django_mako_plus controller handles every request - this line is the glue that connects Mako to Django
    url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),
)



# redirect errors to homepage

handler404 = homepage.views.errors.error404