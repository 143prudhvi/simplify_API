from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^tbgr/$', views.TBGRApi),
    url(r'^tbgr/([0-9]+)$', views.TBGRApi),
    url(r'^board/$', views.BoardApi),
    url(r'^village/$', views.VillageApi),
    url(r'^village/([0-9]+)$', views.VillageApi),
    url(r'^card/$', views.SlipApi),
    url(r'^card/([0-9]+)$', views.SlipApi),
    url(r'^grade/$', views.GradeApi),
    url(r'contact/$', views.ContactApi),
    url(r'^contact/([0-9]+)$', views.ContactApi),
]
