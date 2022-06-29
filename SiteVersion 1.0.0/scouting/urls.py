from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^scoutdata/$', views.ScoutView, name='scoutdata'),
    url(r'^scouttable/(?P<script>[\w-]+)/$', views.ScoutDetailView, name='teamdata'),
  	url(r'^scouttable/$', views.ScoutTableView, name='scouttable'),
    url(r'^scouttable/(?P<script>[\w-]+)/edit/$', views.ScoutEditView, name='editdata'),
    url(r'^events/(?P<slug>[\w-]+)/$', views.EventView, name='eventdetails'),
    url(r'^scouttable/addmatch$', views.MatchAddView, name='addmatch'),
	url(r'^years/$', views.YearView, name='year'),
	url(r'^events/$', views.EventView, name='event'),


]