from django.conf.urls.defaults import *
from foos.views import list, addfoo, editfoo, deletefoo

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', list, name='list'),
    url(r'^add_foo', addfoo, name='add_foo'),
    url(r'^edit/(?P<foo_id>[0-9]*)', editfoo, name='edit_foo'),
    url(r'^delete/(?P<foo_id>[0-9]*)', deletefoo, name='delete_foo'),
)
