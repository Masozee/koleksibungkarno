from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.sitemaps.views import sitemap



#from homepage import views as homepageviews
from search import views as searchviews

from singgasanaseni.views import TagListView

from django.contrib import admin
from .sitemaps import *

# Admin Site Config
admin.sites.AdminSite.site_header = 'Singgasana Seni'
admin.sites.AdminSite.site_title = 'Singgasana Seni'
admin.sites.AdminSite.index_title = 'Singgasana Seni'

# Sitemaps
sitemaps = {
    'karya': KaryaSitemap(),
    'perupa': PerupaSitemap(),
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),

    #multisite
    path('', include('singgasanaseni.urls')),
    path('en/', include('ensites.urls')),
    path('ch/', include('chsites.urls')),

    #thirdparty
    re_path(r'^tagged/(?P<slug>[-\w]+)/$', TagListView.as_view(), name="tagged"),
    path('accounts/', include('django.contrib.auth.urls')),

    #URL untuk sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    #URL Robots
    path('robots.txt', include('robots.urls'), name="robots"),



]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)