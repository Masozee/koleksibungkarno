from django.urls import path, re_path
from django.contrib.auth.decorators import login_required



from search import views as searchviews
from chsites import views as chsitesview




urlpatterns = [

    path('', chsitesview.chindex, name='homepage-ch'),
    path('search/', searchviews.SearchView.as_view(), name='searching-ch' ),
    path('aboutus/', chsitesview.aboutus, name='aboutus-ch'),

    # karya udah aktiv--------------------------------------------------------------------------------------------------
    path('artworks/', chsitesview.Artlist, name='art-list'),

    path('artworks/paintings/', chsitesview.Paintinglist, name='Painting-list'),
    path('artworks/statues/', chsitesview.Statuelist, name='Statue-list'),
    path('artworks/crafts/', chsitesview.Craftlist, name='Craft-list'),

    path('artworks/paintings/landscape/', chsitesview.landscapelist, name='landscape-list'),
    path('artworks/paintings/potraits-and-sensuality/', chsitesview.Potraitlist, name='potrait-list'),
    path('artworks/paintings/still-life/', chsitesview.Naturelist, name='nature-list'),
    path('artworks/paintings/warfare-and-potraits-of-heroes/', chsitesview.Heroeslist, name='heroes-list'),
    path('artworks/paintings/tradition-culture-mythology-activities/', chsitesview.traditionlist, name='tradition-list'),
    path('artworks/paintings/nude/', login_required(chsitesview.nudelist)),
    path('artworks/paintings/nude/', login_required(chsitesview.nudelist)),

    re_path(r'^artworks/(?P<karya_id>\d+)/$', chsitesview.Artdetail, name='art-detail'),

    #koleksi isinya kumpulan perupa ------------------------------------------------------------------------------------
    path('collection/artists/', chsitesview.PainterArtist, name='painter-list'),
    path('collection/sculptor/', chsitesview.Sculptorlist, name='sculptor-list'),
    path('collection/craftsman/', chsitesview.Craftmanlist, name='craftman-list'),


    #Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/painter/A/', chsitesview.AArtist, name='A-artist'),
    path('collection/painter/B/', chsitesview.BArtist, name='B-artist'),
    path('collection/painter/C/', chsitesview.CArtist, name='C-artist'),
    path('collection/painter/D/', chsitesview.DArtist, name='D-artist'),
    path('collection/painter/E/', chsitesview.EArtist, name='E-artist'),
    path('collection/painter/F/', chsitesview.FArtist, name='F-artist'),
    path('collection/painter/G/', chsitesview.GArtist, name='G-artist'),
    path('collection/painter/H/', chsitesview.HArtist, name='H-artist'),
    path('collection/painter/I/', chsitesview.IArtist, name='I-artist'),
    path('collection/painter/J/', chsitesview.JArtist, name='J-artist'),
    path('collection/painter/K/', chsitesview.KArtist, name='K-artist'),
    path('collection/painter/L/', chsitesview.LArtist, name='L-artist'),
    path('collection/painter/M/', chsitesview.MArtist, name='M-artist'),
    path('collection/painter/N/', chsitesview.NArtist, name='N-artist'),
    path('collection/painter/O/', chsitesview.OArtist, name='O-artist'),
    path('collection/painter/P/', chsitesview.PArtist, name='P-artist'),
    path('collection/painter/Q/', chsitesview.QArtist, name='Q-artist'),
    path('collection/painter/R/', chsitesview.RArtist, name='R-artist'),
    path('collection/painter/S/', chsitesview.SArtist, name='S-artist'),
    path('collection/painter/T/', chsitesview.TArtist, name='T-artist'),
    path('collection/painter/U/', chsitesview.UArtist, name='U-artist'),
    path('collection/painter/V/', chsitesview.VArtist, name='V-artist'),
    path('collection/painter/W/', chsitesview.WArtist, name='W-artist'),
    path('collection/painter/X/', chsitesview.XArtist, name='X-artist'),
    path('collection/painter/Y/', chsitesview.YArtist, name='Y-artist'),
    path('collection/painter/Z/', chsitesview.ZArtist, name='Z-artist'),


#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/sculptor/A/', chsitesview.ASculptor, name='A-sculptor'),
    path('collection/sculptor/B/', chsitesview.BSculptor, name='B-sculptor'),
    path('collection/sculptor/C/', chsitesview.CSculptor, name='C-sculptor'),
    path('collection/sculptor/D/', chsitesview.DSculptor, name='D-sculptor'),
    path('collection/sculptor/E/', chsitesview.ESculptor, name='E-sculptor'),
    path('collection/sculptor/F/', chsitesview.FSculptor, name='F-sculptor'),
    path('collection/sculptor/G/', chsitesview.GSculptor, name='G-sculptor'),
    path('collection/sculptor/H/', chsitesview.HSculptor, name='H-sculptor'),
    path('collection/sculptor/I/', chsitesview.ISculptor, name='I-sculptor'),
    path('collection/sculptor/J/', chsitesview.JSculptor, name='J-sculptor'),
    path('collection/sculptor/K/', chsitesview.KSculptor, name='K-sculptor'),
    path('collection/sculptor/L/', chsitesview.LSculptor, name='L-sculptor'),
    path('collection/sculptor/M/', chsitesview.MSculptor, name='M-sculptor'),
    path('collection/sculptor/N/', chsitesview.NSculptor, name='N-sculptor'),
    path('collection/sculptor/O/', chsitesview.OSculptor, name='O-sculptor'),
    path('collection/sculptor/P/', chsitesview.PSculptor, name='P-sculptor'),
    path('collection/sculptor/Q/', chsitesview.QSculptor, name='Q-sculptor'),
    path('collection/sculptor/R/', chsitesview.RSculptor, name='R-sculptor'),
    path('collection/sculptor/S/', chsitesview.SSculptor, name='S-sculptor'),
    path('collection/sculptor/T/', chsitesview.TSculptor, name='T-sculptor'),
    path('collection/sculptor/U/', chsitesview.USculptor, name='U-sculptor'),
    path('collection/sculptor/V/', chsitesview.VSculptor, name='V-sculptor'),
    path('collection/sculptor/W/', chsitesview.WSculptor, name='W-sculptor'),
    path('collection/sculptor/X/', chsitesview.XSculptor, name='X-sculptor'),
    path('collection/sculptor/Y/', chsitesview.YSculptor, name='Y-sculptor'),
    path('collection/sculptor/Z/', chsitesview.ZSculptor, name='Z-sculptor'),

#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/craftsman/A/', chsitesview.ACraft, name='A-craft'),
    path('collection/craftsman/B/', chsitesview.BCraft, name='B-craft'),
    path('collection/craftsman/C/', chsitesview.CCraft, name='C-craft'),
    path('collection/craftsman/D/', chsitesview.DCraft, name='D-craft'),
    path('collection/craftsman/E/', chsitesview.ECraft, name='E-craft'),
    path('collection/craftsman/F/', chsitesview.FCraft, name='F-craft'),
    path('collection/craftsman/G/', chsitesview.GCraft, name='G-craft'),
    path('collection/craftsman/H/', chsitesview.HCraft, name='H-craft'),
    path('collection/craftsman/I/', chsitesview.ICraft, name='I-craft'),
    path('collection/craftsman/J/', chsitesview.JCraft, name='J-craft'),
    path('collection/craftsman/K/', chsitesview.KCraft, name='K-craft'),
    path('collection/craftsman/L/', chsitesview.LCraft, name='L-craft'),
    path('collection/craftsman/M/', chsitesview.MCraft, name='M-craft'),
    path('collection/craftsman/N/', chsitesview.NCraft, name='N-craft'),
    path('collection/craftsman/O/', chsitesview.OCraft, name='O-craft'),
    path('collection/craftsman/P/', chsitesview.PCraft, name='P-craft'),
    path('collection/craftsman/Q/', chsitesview.QCraft, name='Q-craft'),
    path('collection/craftsman/R/', chsitesview.RCraft, name='R-craft'),
    path('collection/craftsman/S/', chsitesview.SCraft, name='S-craft'),
    path('collection/craftsman/T/', chsitesview.TCraft, name='T-craft'),
    path('collection/craftsman/U/', chsitesview.UCraft, name='U-craft'),
    path('collection/craftsman/V/', chsitesview.VCraft, name='V-craft'),
    path('collection/craftsman/W/', chsitesview.WCraft, name='W-craft'),
    path('collection/craftsman/X/', chsitesview.XCraft, name='X-craft'),
    path('collection/craftsman/Y/', chsitesview.YCraft, name='Y-craft'),
    path('collection/craftsman/Z/', chsitesview.ZCraft, name='Z-craft'),

    #Perupa detail -----------------------------------------------------------------------------------------------------______
    re_path(r'^artists/(?P<perupa_id>\d+)/$', chsitesview.Artistsdetail, name='artist-detail'),

    path('news/', chsitesview.Newslist, name='news-list'),

    path('palace/bogor', chsitesview.PalaceBogor, name='palace-bogor'),
    path('palace/cipanas', chsitesview.PalaceCipanas, name='palace-cipanas'),
    path('palace/merdeka', chsitesview.PalaceMerdeka, name='palace-merdeka'),
    path('palace/istananegara', chsitesview.PalaceNegara, name='palace-negara'),
    path('palace/tampaksiring', chsitesview.PalaceTampakSiring, name='palace-tampaksiring'),
    path('palace/yogyakarta', chsitesview.PalaceYogya, name='palace-yogyakarta'),

]

