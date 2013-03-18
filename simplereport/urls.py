from django.conf.urls.defaults import *

from simplereport.views import index, detail

urlpatterns=patterns('',
    (r'^$', index),
    
    (r'^detail/(?P<report_id>\d+)/$', detail),
)