from django.shortcuts import render,  Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from singgasanaseni.models import perupa, karya, berita





#perupa-----------------------------------------------------------------------------------------------
def PerupaList(request):
    Perupa = perupa.objects.filter(Kategori='Pelukis')
    query = request.GET.get("q")
    if query:
        Perupa = Perupa.filter(Nama__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Perupa, 20)
    page = request.GET.get(Page_request_var)
    try:
        Perupa = paginator.page(page)
    except PageNotAnInteger:
        Perupa = paginator.page(1)
    except EmptyPage:
        Perupa = paginator.page(paginator.num_pages)

    context = {
        "perupa":Perupa,
        "page_request_var": Page_request_var
    }

    return render(request, 'perupa/index.html', context)

def Pematunglist(request):
    Pematung = perupa.object.filter(Kategori='Pematung')
    query = request.GET.get("q")
    if query:
        Pematung = Pematung.filter(Nama__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Pematung, 16)
    page = request.GET.get(Page_request_var)
    try:
        Pematung = paginator.page(page)
    except PageNotAnInteger:
        Pematung = paginator.page(1)
    except EmptyPage:
        Pematung = paginator.page(paginator.num_pages)

    context = {
        "pematung":Pematung,
        "page_request_var": Page_request_var
    }

    return render(request, 'perupa/indexpatung.html', context)

def Kriyalist(request):
    Pengrajin = perupa.object.filter(Kategori='Pengrajin')
    query = request.GET.get("q")
    if query:
        Pengrajin = Pengrajin.filter(Nama__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Pengrajin, 16)
    page = request.GET.get(Page_request_var)
    try:
        Pengrajin = paginator.page(page)
    except PageNotAnInteger:
        Pengrajin = paginator.page(1)
    except EmptyPage:
        Pengrajin = paginator.page(paginator.num_pages)

    context = {
        "pengrajin":Pengrajin,
        "page_request_var": Page_request_var
    }

    return render(request, 'perupa/indexkriya.html', context)


def Perupadetail(request, perupa_id):
    try:
        Perupa = perupa.object.get(pk=perupa_id)
    except perupa.DoesNotExist:
        raise Http404('404.html')

    karyarelated = karya.object.filter(Perupa__id=Perupa.id)
    total = karyarelated.count()

    paginator = Paginator(karyarelated, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        Karyarelated = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        Karyarelated = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Karyarelated = paginator.page(paginator.num_pages)

    context={
        "Perupa": Perupa,
        "Karyarelated": Karyarelated,
        "total":total
    }

    return render(request, 'perupa/detail.html', context)

#Karya-------------------------------------------------------------------------------------
def karyalist(request):
    Karya = karya.object.all()
    query = request.GET.get("q")
    if query:
        Karya = Karya.filter(Judul__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Karya, 12)
    page = request.GET.get(Page_request_var)

    try:
        Karya = paginator.page(page)
    except PageNotAnInteger:
        Karya = paginator.page(1)
    except EmptyPage:
        Karya = paginator.page(paginator.num_pages)

    context = {
        "karya": Karya,
        "page_request_var": Page_request_var,

    }

    return render(request, 'karya/index.html', context)


def karyadetail(request, karya_id):
    try:
        Karya = karya.object.get(pk=karya_id)
    except Perupa.DoesNotExist:
        raise Http404('Data karya Belum Tersedia')


    context={
        "Karya": Karya,
    }

    return render(request, 'karya/detail.html', context)

#berita-------------------------------------------------------------------------------
def Beritalist(request):
    Berita = berita.object.all()
    return render(request, 'berita/index.html', {'Berita': Berita})


"""def Beritadetail(request, berita_id):
    try:
        Berita = berita.objects.get(pk=berita_id)
    except berita.DoesNotExist:
        raise Http404('berita Belum Tersedia')

    return render(request, 'berita/detail.html', context={'Berita': Berita})"""

#istana-------------------------------------
def IstanaBogor(request):
    return render(request, 'istana/istanabogor.html' )

def IstanaNegara(request):
    return render(request, 'istana/istananegara.html' )

def IstanaCipanas(request):
    return render(request, 'istana/istanacipanas.html' )

def IstanaMerdeka(request):
    return render(request, 'istana/istanamerdeka.html' )

def IstanaTampakSiring(request):
    return render(request, 'istana/istanatampaksiring.html' )

def IstanaYogya(request):
    return render(request, 'istana/istanayogyakarta.html' )








