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

    path('en/', include('ensites.urls')),

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


#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('koleksi/patung/A/', singgasanaseniviews.APatung, name='A-patung'),
    path('koleksi/patung/B/', singgasanaseniviews.BPatung, name='B-patung'),
    path('koleksi/patung/C/', singgasanaseniviews.CPatung, name='C-patung'),
    path('koleksi/patung/D/', singgasanaseniviews.DPatung, name='D-patung'),
    path('koleksi/patung/E/', singgasanaseniviews.EPatung, name='E-patung'),
    path('koleksi/patung/F/', singgasanaseniviews.FPatung, name='F-patung'),
    path('koleksi/patung/G/', singgasanaseniviews.GPatung, name='G-patung'),
    path('koleksi/patung/H/', singgasanaseniviews.HPatung, name='H-patung'),
    path('koleksi/patung/I/', singgasanaseniviews.IPatung, name='I-patung'),
    path('koleksi/patung/J/', singgasanaseniviews.JPatung, name='J-patung'),
    path('koleksi/patung/K/', singgasanaseniviews.KPatung, name='K-patung'),
    path('koleksi/patung/L/', singgasanaseniviews.LPatung, name='L-patung'),
    path('koleksi/patung/M/', singgasanaseniviews.MPatung, name='M-patung'),
    path('koleksi/patung/N/', singgasanaseniviews.NPatung, name='N-patung'),
    path('koleksi/patung/O/', singgasanaseniviews.OPatung, name='O-patung'),
    path('koleksi/patung/P/', singgasanaseniviews.PPatung, name='P-patung'),
    path('koleksi/patung/Q/', singgasanaseniviews.QPatung, name='Q-patung'),
    path('koleksi/patung/R/', singgasanaseniviews.RPatung, name='R-patung'),
    path('koleksi/patung/S/', singgasanaseniviews.SPatung, name='S-patung'),
    path('koleksi/patung/T/', singgasanaseniviews.TPatung, name='T-patung'),
    path('koleksi/patung/U/', singgasanaseniviews.UPatung, name='U-patung'),
    path('koleksi/patung/V/', singgasanaseniviews.VPatung, name='V-patung'),
    path('koleksi/patung/W/', singgasanaseniviews.WPatung, name='W-patung'),
    path('koleksi/patung/X/', singgasanaseniviews.XPatung, name='X-patung'),
    path('koleksi/patung/Y/', singgasanaseniviews.YPatung, name='Y-patung'),
    path('koleksi/patung/Z/', singgasanaseniviews.ZPatung, name='Z-patung'),

#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('koleksi/kriya/A/', singgasanaseniviews.AKriya, name='A-kriya'),
    path('koleksi/kriya/B/', singgasanaseniviews.BKriya, name='B-kriya'),
    path('koleksi/kriya/C/', singgasanaseniviews.CKriya, name='C-kriya'),
    path('koleksi/kriya/D/', singgasanaseniviews.DKriya, name='D-kriya'),
    path('koleksi/kriya/E/', singgasanaseniviews.EKriya, name='E-kriya'),
    path('koleksi/kriya/F/', singgasanaseniviews.FKriya, name='F-kriya'),
    path('koleksi/kriya/G/', singgasanaseniviews.GKriya, name='G-kriya'),
    path('koleksi/kriya/H/', singgasanaseniviews.HKriya, name='H-kriya'),
    path('koleksi/kriya/I/', singgasanaseniviews.IKriya, name='I-kriya'),
    path('koleksi/kriya/J/', singgasanaseniviews.JKriya, name='J-kriya'),
    path('koleksi/kriya/K/', singgasanaseniviews.KKriya, name='K-kriya'),
    path('koleksi/kriya/L/', singgasanaseniviews.LKriya, name='L-kriya'),
    path('koleksi/kriya/M/', singgasanaseniviews.Mkriya, name='M-kriya'),
    path('koleksi/kriya/N/', singgasanaseniviews.NKriya, name='N-kriya'),
    path('koleksi/kriya/O/', singgasanaseniviews.OKriya, name='O-kriya'),
    path('koleksi/kriya/P/', singgasanaseniviews.PKriya, name='P-kriya'),
    path('koleksi/kriya/Q/', singgasanaseniviews.QKriya, name='Q-kriya'),
    path('koleksi/kriya/R/', singgasanaseniviews.RKriya, name='R-kriya'),
    path('koleksi/kriya/S/', singgasanaseniviews.SKriya, name='S-kriya'),
    path('koleksi/kriya/T/', singgasanaseniviews.TKriya, name='T-kriya'),
    path('koleksi/kriya/U/', singgasanaseniviews.UKriya, name='U-kriya'),
    path('koleksi/kriya/V/', singgasanaseniviews.VKriya, name='V-kriya'),
    path('koleksi/kriya/W/', singgasanaseniviews.WKriya, name='W-kriya'),
    path('koleksi/kriya/X/', singgasanaseniviews.XKriya, name='X-kriya'),
    path('koleksi/kriya/Y/', singgasanaseniviews.YKriya, name='Y-kriya'),
    path('koleksi/kriya/Z/', singgasanaseniviews.ZKriya, name='Z-kriya'),

    #Perupa detail -----------------------------------------------------------------------------------------------------______
    re_path(r'^perupa/(?P<perupa_id>\d+)/$', singgasanaseniviews.Perupadetail, name='perupa-detail'),

    path('berita/', singgasanaseniviews.Beritalist, name='berita-list'),

    path('palace/bogor', singgasanaseniviews.IstanaBogor, name='palace-bogor'),
    path('palace/cipanas', singgasanaseniviews.IstanaCipanas, name='palace-cipanas'),
    path('palace/merdeka', singgasanaseniviews.IstanaMerdeka, name='palace-merdeka'),
    path('palace/istananegara', singgasanaseniviews.IstanaNegara, name='palace-negara'),
    path('palace/tampaksiring', singgasanaseniviews.IstanaTampakSiring, name='palace-tampaksiring'),
    path('palace/yogyakarta', singgasanaseniviews.IstanaYogya, name='palace-yogyakarta'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)