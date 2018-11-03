from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


from singgasanaseni import views as singgasanaseniviews
from homepage import views as homepageviews

from django.contrib import admin

# Admin Site Config
admin.sites.AdminSite.site_header = 'Singgasana Seni'
admin.sites.AdminSite.site_title = 'Singgasana Seni'
admin.sites.AdminSite.index_title = 'Singgasana Seni'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageviews.index, name='homepage-views'),
    path('tentangkami/', homepageviews.tentangkami, name='tentang-kami'),
    path('karya/', singgasanaseniviews.karyalist, name='karya-list'),
    #path('karya/lukisan', singgasanaseniviews.lukisanlist, name='lukisan-list'),
    #path('karya/kriya', singgasanaseniviews.kriyalist, name='kriya-list'),
    #path('karya/patung', singgasanaseniviews.patunglist, name='patung-list'),
    path('perupa/', singgasanaseniviews.PerupaList, name='perupa-list'),
    re_path(r'^perupa/(?P<perupa_id>\d+)/$', singgasanaseniviews.Perupadetail, name='perupa-detail'),
    path('berita/', singgasanaseniviews.Acaralist, name='acara-list'),
    re_path(r'^acara/(?P<acara_id>\d+)/$', singgasanaseniviews.acaradetail, name='acara-detail'),
    path('istana/', singgasanaseniviews.Istanalist, name='istana-list'),
    re_path(r'^istana/(?P<istana_id>\d+)/$', singgasanaseniviews.Istanadetail, name='istana-detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)