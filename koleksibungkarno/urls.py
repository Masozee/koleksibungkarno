from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


from singgasanaseni import views as singgasanaseniviews
from homepage import views as homepageviews
from search import views as searchviews


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

    # karya udah aktiv--------------------------------------------------------------------------------------------------
    path('karya/', singgasanaseniviews.karyalist, name='karya-list'),

    path('karya/lukisan/', singgasanaseniviews.lukisanlist, name='lukisan-list'),
    path('karya/patung/', singgasanaseniviews.Patunglist, name='patung-list'),
    path('karya/kriya/', singgasanaseniviews.kriyalist, name='kriya-list'),

    path('karya/lukisan/pemandangan-alam-dan-kota/', singgasanaseniviews.alamkotalist, name='alamkota-list'),
    path('karya/lukisan/potret-dan-sensualitas/', singgasanaseniviews.potretlist, name='potret-list'),
    path('karya/lukisan/alam-dan-benda/', singgasanaseniviews.alamlist, name='alam-list'),
    path('karya/lukisan/perjuangan-dan-potret-para-pejuang/', singgasanaseniviews.juanglist, name='juang-list'),
    path('karya/lukisan/tradisi-budaya-mitologi-keseharian/', singgasanaseniviews.tradisilist, name='tradisi-list'),

    re_path(r'^karya/(?P<karya_id>\d+)/$', singgasanaseniviews.karyadetail, name='karya-detail'),

    #koleksi isinya kumpulan perupa ------------------------------------------------------------------------------------
    path('koleksi/lukisan/', singgasanaseniviews.PerupaList, name='Perupa-list'),
    path('koleksi/patung/', singgasanaseniviews.Pematunglist, name='Pematung-list'),
    path('koleksi/kriya/', singgasanaseniviews.Pengrajinlist, name='Pengrajin-list'),


    #Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('koleksi/lukisan/A/', singgasanaseniviews.AList, name='A-list'),
    path('koleksi/lukisan/B/', singgasanaseniviews.BList, name='B-list'),
    path('koleksi/lukisan/C/', singgasanaseniviews.CList, name='C-list'),
    path('koleksi/lukisan/D/', singgasanaseniviews.DList, name='D-list'),
    path('koleksi/lukisan/E/', singgasanaseniviews.EList, name='E-list'),
    path('koleksi/lukisan/F/', singgasanaseniviews.FList, name='F-list'),
    path('koleksi/lukisan/G/', singgasanaseniviews.GList, name='G-list'),
    path('koleksi/lukisan/H/', singgasanaseniviews.HList, name='H-list'),
    path('koleksi/lukisan/I/', singgasanaseniviews.IList, name='I-list'),
    path('koleksi/lukisan/J/', singgasanaseniviews.JList, name='J-list'),
    path('koleksi/lukisan/K/', singgasanaseniviews.KList, name='K-list'),
    path('koleksi/lukisan/L/', singgasanaseniviews.LList, name='L-list'),
    path('koleksi/lukisan/M/', singgasanaseniviews.MList, name='M-list'),
    path('koleksi/lukisan/N/', singgasanaseniviews.NList, name='N-list'),
    path('koleksi/lukisan/O/', singgasanaseniviews.OList, name='O-list'),
    path('koleksi/lukisan/P/', singgasanaseniviews.PList, name='P-list'),
    path('koleksi/lukisan/Q/', singgasanaseniviews.QList, name='Q-list'),
    path('koleksi/lukisan/R/', singgasanaseniviews.RList, name='R-list'),
    path('koleksi/lukisan/S/', singgasanaseniviews.SList, name='S-list'),
    path('koleksi/lukisan/T/', singgasanaseniviews.TList, name='T-list'),
    path('koleksi/lukisan/U/', singgasanaseniviews.UList, name='U-list'),
    path('koleksi/lukisan/V/', singgasanaseniviews.VList, name='V-list'),
    path('koleksi/lukisan/W/', singgasanaseniviews.WList, name='W-list'),
    path('koleksi/lukisan/X/', singgasanaseniviews.XList, name='X-list'),
    path('koleksi/lukisan/Y/', singgasanaseniviews.YList, name='Y-list'),
    path('koleksi/lukisan/Z/', singgasanaseniviews.ZList, name='Z-list'),



    #Perupa detail -----------------------------------------------------------------------------------------------------______
    re_path(r'^perupa/(?P<perupa_id>\d+)/$', singgasanaseniviews.Perupadetail, name='perupa-detail'),

    path('berita/', singgasanaseniviews.Beritalist, name='berita-list'),

    path('istana/bogor', singgasanaseniviews.IstanaBogor, name='istana-bogor'),
    path('istana/cipanas', singgasanaseniviews.IstanaCipanas, name='istana-cipanas'),
    path('istana/merdeka', singgasanaseniviews.IstanaMerdeka, name='istana-merdeka'),
    path('istana/istananegara', singgasanaseniviews.IstanaNegara, name='istana-negara'),
    path('istana/tampaksiring', singgasanaseniviews.IstanaTampakSiring, name='istana-tampaksiring'),
    path('istana/yogyakarta', singgasanaseniviews.IstanaYogya, name='istana-yogyakarta'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)