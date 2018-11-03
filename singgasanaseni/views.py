from django.shortcuts import render,  Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import perupa, karya, acara, istana, kurator

#perupa-----------------------------------------------------------------------------------------------
def PerupaList(request):
    Perupa = perupa.objects.all()
    query = request.GET.get("q")
    if query:
        Perupa = Perupa.filter(Nama__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Perupa, 16)
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


def Perupadetail(request, perupa_id):
    try:
        Perupa = perupa.objects.get(pk=perupa_id)
    except Perupa.DoesNotExist:
        raise Http404('Data Perupa Belum Tersedia')

    karyarelated = karya.objects.filter(Perupa__karya=Perupa.id)

    context={
        "Perupa": Perupa,
        "Karya": karyarelated
    }

    return render(request, 'perupa/detail.html', context)

#Karya-------------------------------------------------------------------------------------
def karyalist(request):
    Karya = karya.objects.all()



    query = request.GET.get("q")
    if query:
        Karya = Karya.filter(Judul__icontains=query)
    Page_request_var = "page"
    paginator = Paginator(Karya, 10)
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


def Karyadetail(request, karya_id):
    try:
        Detail = karya.objects.get(pk=karya_id)
    except karya.DoesNotExist:
        raise Http404('data Karya belum tersedia')

    return render(request, 'karya/index.html', context={'detail': Detail})


#acara-------------------------------------------------------------------------------
def Acaralist(request):
    Acara = acara.objects.all()
    return render(request, 'acara/index.html', {'Acara': Acara})


def acaradetail(request, acara_id):
    try:
        Acara = acara.objects.get(pk=acara_id)
    except lukisan.DoesNotExist:
        raise Http404('Acara Belum Tersedia')

    return render(request, 'acara/detail.html', context={'Acara': Acara})

#istana-------------------------------------
def Istanalist(request):
    Istana = istana.objects.all()
    return render(request, 'istana/index.html', {'Istana': Istana})


def Istanadetail(request, istana_id):
    try:
        Istana = istana.objects.get(pk=istana_id)
    except istana.DoesNotExist:
        raise Http404('Data Tidak tersedia')

    return render(request, 'istana/detail.html', context={'Istana': Istana})

#kurator-----------------------------------------
def Kuratorlist(request):
    Kurator = kurator.objects.all()
    return render(request, 'kurator/index.html', {'Kurator': Kurator})


def KuratorDetail(request, kurator_id):
    try:
        Kurator = kurator.objects.get(pk=kurator_id)
    except kurator.DoesNotExist:
        raise Http404('Acara Belum Tersedia')

    return render(request, 'kurator/detail.html', context={'Kurator': Kurator})