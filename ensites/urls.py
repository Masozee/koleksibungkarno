from django.urls import path, re_path
from django.contrib.auth.decorators import login_required



from search import views as searchviews
from ensites import views as sitesviews




urlpatterns = [

    path('', sitesviews.enindex, name='homepage-en'),
    path('search/', searchviews.SearchView.as_view(), name='searching' ),
    path('aboutus/', sitesviews.aboutus, name='aboutus'),

    # karya udah aktiv--------------------------------------------------------------------------------------------------
    path('artworks/', sitesviews.Artlist, name='art-list'),

    path('artworks/paintings/', sitesviews.Paintinglist, name='Painting-list'),
    path('artworks/statues/', sitesviews.Statuelist, name='Statue-list'),
    path('artworks/crafts/', sitesviews.Craftlist, name='Craft-list'),

    path('artworks/paintings/landscape/', sitesviews.landscapelist, name='landscape-list'),
    path('artworks/paintings/potraits-and-sensuality/', sitesviews.Potraitlist, name='potrait-list'),
    path('artworks/paintings/still-life/', sitesviews.Naturelist, name='nature-list'),
    path('artworks/paintings/warfare-and-potraits-of-heroes/', sitesviews.Heroeslist, name='heroes-list'),
    path('artworks/paintings/tradition-culture-mythology-activities/', sitesviews.traditionlist, name='tradition-list'),
    path('artworks/paintings/nude/', login_required(sitesviews.nudelist)),


    re_path(r'^artworks/(?P<karya_id>\d+)/$', sitesviews.Artdetail, name='art-detail'),

    #koleksi isinya kumpulan perupa ------------------------------------------------------------------------------------
    path('collection/artists/', sitesviews.PainterArtist, name='painter-list'),
    path('collection/sculptor/', sitesviews.Sculptorlist, name='sculptor-list'),
    path('collection/craftsman/', sitesviews.Craftmanlist, name='craftman-list'),


    #Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/painter/A/', sitesviews.AArtist, name='A-artist'),
    path('collection/painter/B/', sitesviews.BArtist, name='B-artist'),
    path('collection/painter/C/', sitesviews.CArtist, name='C-artist'),
    path('collection/painter/D/', sitesviews.DArtist, name='D-artist'),
    path('collection/painter/E/', sitesviews.EArtist, name='E-artist'),
    path('collection/painter/F/', sitesviews.FArtist, name='F-artist'),
    path('collection/painter/G/', sitesviews.GArtist, name='G-artist'),
    path('collection/painter/H/', sitesviews.HArtist, name='H-artist'),
    path('collection/painter/I/', sitesviews.IArtist, name='I-artist'),
    path('collection/painter/J/', sitesviews.JArtist, name='J-artist'),
    path('collection/painter/K/', sitesviews.KArtist, name='K-artist'),
    path('collection/painter/L/', sitesviews.LArtist, name='L-artist'),
    path('collection/painter/M/', sitesviews.MArtist, name='M-artist'),
    path('collection/painter/N/', sitesviews.NArtist, name='N-artist'),
    path('collection/painter/O/', sitesviews.OArtist, name='O-artist'),
    path('collection/painter/P/', sitesviews.PArtist, name='P-artist'),
    path('collection/painter/Q/', sitesviews.QArtist, name='Q-artist'),
    path('collection/painter/R/', sitesviews.RArtist, name='R-artist'),
    path('collection/painter/S/', sitesviews.SArtist, name='S-artist'),
    path('collection/painter/T/', sitesviews.TArtist, name='T-artist'),
    path('collection/painter/U/', sitesviews.UArtist, name='U-artist'),
    path('collection/painter/V/', sitesviews.VArtist, name='V-artist'),
    path('collection/painter/W/', sitesviews.WArtist, name='W-artist'),
    path('collection/painter/X/', sitesviews.XArtist, name='X-artist'),
    path('collection/painter/Y/', sitesviews.YArtist, name='Y-artist'),
    path('collection/painter/Z/', sitesviews.ZArtist, name='Z-artist'),


#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/sculptor/A/', sitesviews.ASculptor, name='A-sculptor'),
    path('collection/sculptor/B/', sitesviews.BSculptor, name='B-sculptor'),
    path('collection/sculptor/C/', sitesviews.CSculptor, name='C-sculptor'),
    path('collection/sculptor/D/', sitesviews.DSculptor, name='D-sculptor'),
    path('collection/sculptor/E/', sitesviews.ESculptor, name='E-sculptor'),
    path('collection/sculptor/F/', sitesviews.FSculptor, name='F-sculptor'),
    path('collection/sculptor/G/', sitesviews.GSculptor, name='G-sculptor'),
    path('collection/sculptor/H/', sitesviews.HSculptor, name='H-sculptor'),
    path('collection/sculptor/I/', sitesviews.ISculptor, name='I-sculptor'),
    path('collection/sculptor/J/', sitesviews.JSculptor, name='J-sculptor'),
    path('collection/sculptor/K/', sitesviews.KSculptor, name='K-sculptor'),
    path('collection/sculptor/L/', sitesviews.LSculptor, name='L-sculptor'),
    path('collection/sculptor/M/', sitesviews.MSculptor, name='M-sculptor'),
    path('collection/sculptor/N/', sitesviews.NSculptor, name='N-sculptor'),
    path('collection/sculptor/O/', sitesviews.OSculptor, name='O-sculptor'),
    path('collection/sculptor/P/', sitesviews.PSculptor, name='P-sculptor'),
    path('collection/sculptor/Q/', sitesviews.QSculptor, name='Q-sculptor'),
    path('collection/sculptor/R/', sitesviews.RSculptor, name='R-sculptor'),
    path('collection/sculptor/S/', sitesviews.SSculptor, name='S-sculptor'),
    path('collection/sculptor/T/', sitesviews.TSculptor, name='T-sculptor'),
    path('collection/sculptor/U/', sitesviews.USculptor, name='U-sculptor'),
    path('collection/sculptor/V/', sitesviews.VSculptor, name='V-sculptor'),
    path('collection/sculptor/W/', sitesviews.WSculptor, name='W-sculptor'),
    path('collection/sculptor/X/', sitesviews.XSculptor, name='X-sculptor'),
    path('collection/sculptor/Y/', sitesviews.YSculptor, name='Y-sculptor'),
    path('collection/sculptor/Z/', sitesviews.ZSculptor, name='Z-sculptor'),

#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/craftsman/A/', sitesviews.ACraft, name='A-craft'),
    path('collection/craftsman/B/', sitesviews.BCraft, name='B-craft'),
    path('collection/craftsman/C/', sitesviews.CCraft, name='C-craft'),
    path('collection/craftsman/D/', sitesviews.DCraft, name='D-craft'),
    path('collection/craftsman/E/', sitesviews.ECraft, name='E-craft'),
    path('collection/craftsman/F/', sitesviews.FCraft, name='F-craft'),
    path('collection/craftsman/G/', sitesviews.GCraft, name='G-craft'),
    path('collection/craftsman/H/', sitesviews.HCraft, name='H-craft'),
    path('collection/craftsman/I/', sitesviews.ICraft, name='I-craft'),
    path('collection/craftsman/J/', sitesviews.JCraft, name='J-craft'),
    path('collection/craftsman/K/', sitesviews.KCraft, name='K-craft'),
    path('collection/craftsman/L/', sitesviews.LCraft, name='L-craft'),
    path('collection/craftsman/M/', sitesviews.MCraft, name='M-craft'),
    path('collection/craftsman/N/', sitesviews.NCraft, name='N-craft'),
    path('collection/craftsman/O/', sitesviews.OCraft, name='O-craft'),
    path('collection/craftsman/P/', sitesviews.PCraft, name='P-craft'),
    path('collection/craftsman/Q/', sitesviews.QCraft, name='Q-craft'),
    path('collection/craftsman/R/', sitesviews.RCraft, name='R-craft'),
    path('collection/craftsman/S/', sitesviews.SCraft, name='S-craft'),
    path('collection/craftsman/T/', sitesviews.TCraft, name='T-craft'),
    path('collection/craftsman/U/', sitesviews.UCraft, name='U-craft'),
    path('collection/craftsman/V/', sitesviews.VCraft, name='V-craft'),
    path('collection/craftsman/W/', sitesviews.WCraft, name='W-craft'),
    path('collection/craftsman/X/', sitesviews.XCraft, name='X-craft'),
    path('collection/craftsman/Y/', sitesviews.YCraft, name='Y-craft'),
    path('collection/craftsman/Z/', sitesviews.ZCraft, name='Z-craft'),

    #Perupa detail -----------------------------------------------------------------------------------------------------______
    re_path(r'^artists/(?P<perupa_id>\d+)/$', sitesviews.Artistsdetail, name='artist-detail'),

    path('news/', sitesviews.Newslist, name='news-list'),

    path('palace/bogor', sitesviews.PalaceBogor, name='palace-bogor'),
    path('palace/cipanas', sitesviews.PalaceCipanas, name='palace-cipanas'),
    path('palace/merdeka', sitesviews.PalaceMerdeka, name='palace-merdeka'),
    path('palace/istananegara', sitesviews.PalaceNegara, name='palace-negara'),
    path('palace/tampaksiring', sitesviews.PalaceTampakSiring, name='palace-tampaksiring'),
    path('palace/yogyakarta', sitesviews.PalaceYogya, name='palace-yogyakarta'),

]

