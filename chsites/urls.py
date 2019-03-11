from django.urls import path, re_path
from django.contrib.auth.decorators import login_required



from search import views as searchviews
from chsites import views as chsitesview




urlpatterns = [

    path('', chsitesview.chindex, name='homepage-ch'),
    path('search/', searchviews.SearchView.as_view(), name='searching-ch' ),
    path('aboutus/', chsitesview.chaboutus, name='aboutus-ch'),

    # karya udah aktiv--------------------------------------------------------------------------------------------------
    path('artworks/', chsitesview.chArtlist, name='art-list-ch'),

    path('artworks/paintings/', chsitesview.chPaintinglist, name='Painting-list-ch'),
    path('artworks/statues/', chsitesview.chStatuelist, name='Statue-list-ch'),
    path('artworks/crafts/', chsitesview.chCraftlist, name='Craft-list-ch'),

    path('artworks/paintings/landscape/', chsitesview.chlandscapelist, name='landscape-list-ch'),
    path('artworks/paintings/potraits-and-sensuality/', chsitesview.chPotraitlist, name='potrait-list-ch'),
    path('artworks/paintings/still-life/', chsitesview.chNaturelist, name='nature-list-ch'),
    path('artworks/paintings/warfare-and-potraits-of-heroes/', chsitesview.chHeroeslist, name='heroes-list-ch'),
    path('artworks/paintings/tradition-culture-mythology-activities/', chsitesview.chtraditionlist, name='tradition-list-ch'),
    path('artworks/paintings/nude/', login_required(chsitesview.chnudelist)),
    path('artworks/paintings/nude/', login_required(chsitesview.chnudelist)),

    re_path(r'^artworks/(?P<karya_id>\d+)/$', chsitesview.chArtdetail, name='art-detail-ch'),

    #koleksi isinya kumpulan perupa ------------------------------------------------------------------------------------
    path('collection/artists/', chsitesview.chPainterArtist, name='painter-list-ch'),
    path('collection/sculptor/', chsitesview.chSculptorlist, name='sculptor-list-ch'),
    path('collection/craftsman/', chsitesview.chCraftmanlist, name='craftman-list-ch'),


    #Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/painter/A/', chsitesview.chAArtist, name='A-artist-ch'),
    path('collection/painter/B/', chsitesview.chBArtist, name='B-artist-ch'),
    path('collection/painter/C/', chsitesview.chCArtist, name='C-artist-ch'),
    path('collection/painter/D/', chsitesview.chDArtist, name='D-artist-ch'),
    path('collection/painter/E/', chsitesview.chEArtist, name='E-artist-ch'),
    path('collection/painter/F/', chsitesview.chFArtist, name='F-artist-ch'),
    path('collection/painter/G/', chsitesview.chGArtist, name='G-artist-ch'),
    path('collection/painter/H/', chsitesview.chHArtist, name='H-artist-ch'),
    path('collection/painter/I/', chsitesview.chIArtist, name='I-artist-ch'),
    path('collection/painter/J/', chsitesview.chJArtist, name='J-artist-ch'),
    path('collection/painter/K/', chsitesview.chKArtist, name='K-artist-ch'),
    path('collection/painter/L/', chsitesview.chLArtist, name='L-artist-ch'),
    path('collection/painter/M/', chsitesview.chMArtist, name='M-artist-ch'),
    path('collection/painter/N/', chsitesview.chNArtist, name='N-artist-ch'),
    path('collection/painter/O/', chsitesview.chOArtist, name='O-artist-ch'),
    path('collection/painter/P/', chsitesview.chPArtist, name='P-artist-ch'),
    path('collection/painter/Q/', chsitesview.chQArtist, name='Q-artist-ch'),
    path('collection/painter/R/', chsitesview.chRArtist, name='R-artist-ch'),
    path('collection/painter/S/', chsitesview.chSArtist, name='S-artist-ch'),
    path('collection/painter/T/', chsitesview.chTArtist, name='T-artist-ch'),
    path('collection/painter/U/', chsitesview.chUArtist, name='U-artist-ch'),
    path('collection/painter/V/', chsitesview.chVArtist, name='V-artist-ch'),
    path('collection/painter/W/', chsitesview.chWArtist, name='W-artist-ch'),
    path('collection/painter/X/', chsitesview.chXArtist, name='X-artist-ch'),
    path('collection/painter/Y/', chsitesview.chYArtist, name='Y-artist-ch'),
    path('collection/painter/Z/', chsitesview.chZArtist, name='Z-artist-ch'),


#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/sculptor/A/', chsitesview.chASculptor, name='A-sculptor-ch'),
    path('collection/sculptor/B/', chsitesview.chBSculptor, name='B-sculptor-ch'),
    path('collection/sculptor/C/', chsitesview.chCSculptor, name='C-sculptor-ch'),
    path('collection/sculptor/D/', chsitesview.chDSculptor, name='D-sculptor-ch'),
    path('collection/sculptor/E/', chsitesview.chESculptor, name='E-sculptor-ch'),
    path('collection/sculptor/F/', chsitesview.chFSculptor, name='F-sculptor-ch'),
    path('collection/sculptor/G/', chsitesview.chGSculptor, name='G-sculptor-ch'),
    path('collection/sculptor/H/', chsitesview.chHSculptor, name='H-sculptor-ch'),
    path('collection/sculptor/I/', chsitesview.chISculptor, name='I-sculptor-ch'),
    path('collection/sculptor/J/', chsitesview.chJSculptor, name='J-sculptor-ch'),
    path('collection/sculptor/K/', chsitesview.chKSculptor, name='K-sculptor-ch'),
    path('collection/sculptor/L/', chsitesview.chLSculptor, name='L-sculptor-ch'),
    path('collection/sculptor/M/', chsitesview.chMSculptor, name='M-sculptor-ch'),
    path('collection/sculptor/N/', chsitesview.chNSculptor, name='N-sculptor-ch'),
    path('collection/sculptor/O/', chsitesview.chOSculptor, name='O-sculptor-ch'),
    path('collection/sculptor/P/', chsitesview.chPSculptor, name='P-sculptor-ch'),
    path('collection/sculptor/Q/', chsitesview.chQSculptor, name='Q-sculptor-ch'),
    path('collection/sculptor/R/', chsitesview.chRSculptor, name='R-sculptor-ch'),
    path('collection/sculptor/S/', chsitesview.chSSculptor, name='S-sculptor-ch'),
    path('collection/sculptor/T/', chsitesview.chTSculptor, name='T-sculptor-ch'),
    path('collection/sculptor/U/', chsitesview.chUSculptor, name='U-sculptor-ch'),
    path('collection/sculptor/V/', chsitesview.chVSculptor, name='V-sculptor-ch'),
    path('collection/sculptor/W/', chsitesview.chWSculptor, name='W-sculptor-ch'),
    path('collection/sculptor/X/', chsitesview.chXSculptor, name='X-sculptor-ch'),
    path('collection/sculptor/Y/', chsitesview.chYSculptor, name='Y-sculptor-ch'),
    path('collection/sculptor/Z/', chsitesview.chZSculptor, name='Z-sculptor-ch'),

#Filtering Alfabet -------------------------------------------------------------------------------------------------
    path('collection/craftsman/A/', chsitesview.chACraft, name='A-craft-ch'),
    path('collection/craftsman/B/', chsitesview.chBCraft, name='B-craft-ch'),
    path('collection/craftsman/C/', chsitesview.chCCraft, name='C-craft-ch'),
    path('collection/craftsman/D/', chsitesview.chDCraft, name='D-craft-ch'),
    path('collection/craftsman/E/', chsitesview.chECraft, name='E-craft-ch'),
    path('collection/craftsman/F/', chsitesview.chFCraft, name='F-craft-ch'),
    path('collection/craftsman/G/', chsitesview.chGCraft, name='G-craft-ch'),
    path('collection/craftsman/H/', chsitesview.chHCraft, name='H-craft-ch'),
    path('collection/craftsman/I/', chsitesview.chICraft, name='I-craft-ch'),
    path('collection/craftsman/J/', chsitesview.chJCraft, name='J-craft-ch'),
    path('collection/craftsman/K/', chsitesview.chKCraft, name='K-craft-ch'),
    path('collection/craftsman/L/', chsitesview.chLCraft, name='L-craft-ch'),
    path('collection/craftsman/M/', chsitesview.chMCraft, name='M-craft-ch'),
    path('collection/craftsman/N/', chsitesview.chNCraft, name='N-craft-ch'),
    path('collection/craftsman/O/', chsitesview.chOCraft, name='O-craft-ch'),
    path('collection/craftsman/P/', chsitesview.chPCraft, name='P-craft-ch'),
    path('collection/craftsman/Q/', chsitesview.chQCraft, name='Q-craft-ch'),
    path('collection/craftsman/R/', chsitesview.chRCraft, name='R-craft-ch'),
    path('collection/craftsman/S/', chsitesview.chSCraft, name='S-craft-ch'),
    path('collection/craftsman/T/', chsitesview.chTCraft, name='T-craft-ch'),
    path('collection/craftsman/U/', chsitesview.chUCraft, name='U-craft-ch'),
    path('collection/craftsman/V/', chsitesview.chVCraft, name='V-craft-ch'),
    path('collection/craftsman/W/', chsitesview.chWCraft, name='W-craft-ch'),
    path('collection/craftsman/X/', chsitesview.chXCraft, name='X-craft-ch'),
    path('collection/craftsman/Y/', chsitesview.chYCraft, name='Y-craft-ch'),
    path('collection/craftsman/Z/', chsitesview.chZCraft, name='Z-craft-ch'),

    #Perupa detail -----------------------------------------------------------------------------------------------------______
    re_path(r'^artists/(?P<perupa_id>\d+)/$', chsitesview.chArtistsdetail, name='artist-detail-ch'),

    path('news/', chsitesview.chNewslist, name='news-list-ch'),

    path('palace/bogor', chsitesview.chPalaceBogor, name='palace-bogor-ch'),
    path('palace/cipanas', chsitesview.chPalaceCipanas, name='palace-cipanas-ch'),
    path('palace/merdeka', chsitesview.chPalaceMerdeka, name='palace-merdeka-ch'),
    path('palace/istananegara', chsitesview.chPalaceNegara, name='palace-negara-ch'),
    path('palace/tampaksiring', chsitesview.chPalaceTampakSiring, name='palace-tampaksiring-ch'),
    path('palace/yogyakarta', chsitesview.chPalaceYogya, name='palace-yogyakarta-ch'),

]

