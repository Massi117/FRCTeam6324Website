#robotpage URL Configuration
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from robotpage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_redirect, name="login_redirect"),
    url(r'^frc6324/', include(('sponsors.urls', 'sponsors'), namespace='sponsors')),
    url(r'^feed/', include(('feed.urls', 'feed'), namespace='feed')),
    url(r'^scouting/', include(('scouting.urls', 'scouting'), namespace='scouting')),
    url(r'^gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
