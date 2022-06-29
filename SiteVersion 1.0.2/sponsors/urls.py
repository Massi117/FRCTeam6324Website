from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^gold/$', views.GoldSponsorView, name='gold_sponsor_page'),
    url(r'^silver/$', views.SilverSponsorView, name='silver_sponsor_page'),
    url(r'^bronze/$', views.BronzeSponsorView, name='bronze_sponsor_page'),
    url(r'^gold/(?P<slug>[\w-]+)/$', views.SponsorDetailView, name='sponsor_detail'),
    url(r'^silver/(?P<slug>[\w-]+)/$', views.SponsorDetailView, name='sponsor_detail'),
    url(r'^bronze/(?P<slug>[\w-]+)/$', views.SponsorDetailView, name='sponsor_detail'),
    url(r'^aboutus/$', views.HistoryView, name='about_us'),
    url(r'^members/$', views.MemberView, name='members'),
    url(r'^become/$', views.BecomeView, name='become'),
    url(r'^community/$', views.CommunityView, name='community'),
    url(r'^contact/$', views.ContactView, name='contact'),
    
    
]