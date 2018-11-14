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
    path('search/', singgasanaseniviews.searchposts, name='search'),
    path('tentangkami/', homepageviews.tentangkami, name='tentang-kami'),
    path('karya/', singgasanaseniviews.karyalist, name='karya-list'),
    re_path(r'^karya/(?P<karya_id>\d+)/$', singgasanaseniviews.karyadetail, name='karya-detail'),
    re_path(r'^karya/(?P<slug>[\w-]+)/$', singgasanaseniviews.karyadetail, name='karya-detail'),
    path('koleksi/lukisan/', singgasanaseniviews.PerupaList, name='perupa-list'),
    path('koleksi/patung/', singgasanaseniviews.Pematunglist, name='Pematung-list'),
    path('koleksi/kriya/', singgasanaseniviews.Kriyalist, name='Pengrajin-list'),
    re_path(r'^perupa/(?P<perupa_id>\d+)/$', singgasanaseniviews.Perupadetail, name='perupa-detail'),
    path('berita/', singgasanaseniviews.Beritalist, name='berita-list'),
    re_path(r'^berita/(?P<berita_id>\d+)/$', singgasanaseniviews.Beritadetail, name='berita-detail'),
    path('istana/bogor', singgasanaseniviews.IstanaBogor, name='istana-bogor'),
    path('istana/cipanas', singgasanaseniviews.IstanaCipanas, name='istana-bogor'),
    path('istana/merdeka', singgasanaseniviews.IstanaMerdeka, name='istana-bogor'),
    path('istana/istananegara', singgasanaseniviews.IstanaNegara, name='istana-bogor'),
    path('istana/tampaksiring', singgasanaseniviews.IstanaTampakSiring, name='istana-bogor'),
    path('istana/yogyakarta', singgasanaseniviews.IstanaYogya, name='istana-bogor'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)