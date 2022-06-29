from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^scoutdata/$', views.ScoutView, name='scoutdata'),
    url(r'^scouttable/(?P<script>[\w-]+)/$', views.ScoutDetailView, name='teamdata'),
  	url(r'^scouttable/$', views.ScoutTableView, name='scouttable'),
    url(r'^scouttable/(?P<script>[\w-]+)/edit/$', views.ScoutEditView, name='editdata'),
    url(r'^scouttable/addmatch$', views.MatchAddView, name='addmatch'),
	url(r'^events/$', views.EventView, name='event'),
	url(r'^scouttable/(?P<script>[\w-]+)/(?P<slug>[\w-]+)/$', views.EventDetailView, name='eventdata'),


]