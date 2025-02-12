from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_mailing/$', views.create_mailing, name='create_mailing'),
]