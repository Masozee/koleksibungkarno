from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


from singgasanaseni import views as singgasanaseniviews
from homepage import views as homepageviews
from search import views as searchviews

from singgasanaseni.views import TagListView

from django.contrib import admin

# Admin Site Config
admin.sites.AdminSite.site_header = 'Singgasana Seni'
admin.sites.AdminSite.site_title = 'Singgasana Seni'
admin.sites.AdminSite.index_title = 'Singgasana Seni'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageviews.index, name='homepage-views'),
    path('search/', searchviews.SearchView.as_view(), name='searching' ),
    path('tentangkami/', homepageviews.tentangkami, name='tentang-kami'),
    path('', include('singgasanaseni.urls')),
    path('en/', include('ensites.urls')),
    re_path(r'^tagged/(?P<slug>[-\w]+)/$', TagListView.as_view(), name="tagged"),
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)