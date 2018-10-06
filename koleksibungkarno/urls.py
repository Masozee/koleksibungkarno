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
    path('', homepageviews.index),
    path('tentangkami/', homepageviews.tentangkami),
    path('karya/', singgasanaseniviews.karyalist),
    re_path(r'^karya/(?P<karya_id>\d+)/$', singgasanaseniviews.Karyadetail),
    path('perupa/', singgasanaseniviews.PerupaList),
    re_path(r'^perupa/(?P<perupa_id>\d+)/$', singgasanaseniviews.Perupadetail),
    path('acara/', singgasanaseniviews.Acaralist),
    re_path(r'^acara/(?P<acara_id>\d+)/$', singgasanaseniviews.acaradetail),
    path('istana/', singgasanaseniviews.Istanalist),
    re_path(r'^istana/(?P<istana_id>\d+)/$', singgasanaseniviews.Istanadetail),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)