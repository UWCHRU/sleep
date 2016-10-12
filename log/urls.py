from django.conf.urls import url

from . import views
from log.views import LogView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', LogView.as_view(), name='log-add'),
]

