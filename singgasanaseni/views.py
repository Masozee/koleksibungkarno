from django.shortcuts import render,  Http404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import perupa, karya, acara, istana, kurator

#perupa-----------------------------------------------------------------------------------------------
def PerupaList(request):
    Perupa = perupa.objects.all()

    page = request.GET.get('page',1)

    paginator = Paginator(Perupa, 10)
    try:
        Perupa = paginator.page(page)
    except PageNotAnInteger:
        Perupa = paginator.page(1)
    except EmptyPage:
        Perupa = paginator.page(paginator.num_pages)

    return render(request, 'perupa/index.html', {'Perupa':Perupa})


def Perupadetail(request, perupa_id):
    Karya = (
        karya.objects.values('Perupa').order_by('Perupa')
    )
    try:
        Perupa = perupa.objects.get(pk=perupa_id)
    except perupa.DoesNotExist:
        raise Http404('Data Perupa Belum Tersedia')

    return render(request, 'perupa/detail.html', context=({'Perupa':Perupa,'Karya':Karya}))

#Karya-------------------------------------------------------------------------------------
def karyalist(request):
    Karya = karya.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(Karya, 10)
    try:
        Karya = paginator.page(page)
    except PageNotAnInteger:
        Karya = paginator.page(1)
    except EmptyPage:
        Karya = paginator.page(paginator.num_pages)

    return render(request, 'karya/index.html', {'Karya': Karya})


def Karyadetail(request, karya_id):
    try:
        Karya = karya.objects.get(pk=karya_id)
    except karya.DoesNotExist:
        raise Http404('data Karya belum tersedia')

    return render(request, 'karya/detail.html', context={'Karya': Karya})

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