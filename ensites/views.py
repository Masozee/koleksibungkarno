from django.shortcuts import render, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from singgasanaseni.models import perupa, karya, berita, HomeSlide
from ensites.models import News


#Slider
def enindex(request):
    Berita = berita.object.all().order_by("-Tanggal")[:4]
    Slide = HomeSlide.objects.all()

    context = {
        "Berita": Berita,
        "Slide": Slide
    }
    return render (request, "homepage/enindex.html", context)

def aboutus(request):
    return render (request, "homepage/aboutus.html")


# Perupa-----------------------------------------------------------------------------------------------
def PainterArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)

def Sculptorlist(request):
	Perupa = perupa.object.filter(Kategori='Pematung').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)

def Craftmanlist(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)

def Artistsdetail(request, perupa_id):
	try:
		Perupa = perupa.object.get(pk=perupa_id)
	except perupa.DoesNotExist:
		raise Http404('404.html')

	Karyarelated = karya.object.filter(Perupa__id=Perupa.id, Perupa__karya__Naked_Material=False).distinct()
	total = Karyarelated.count()

	paginator = Paginator(Karyarelated, 20)  # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		Karyarelated = paginator.page(page)
	except PageNotAnInteger:
		Karyarelated = paginator.page(1)
	except EmptyPage:
		Karyarelated = paginator.page(paginator.num_pages)

	context = {
		"Perupa": Perupa,
		"Karyarelated": Karyarelated,
		"total": total
	}

	return render(request, 'artists/detail.html', context)

#filtering perupa --------------
def AArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'A').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def BArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'B').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def CArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'C').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def DArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'D').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def EArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'E').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def FArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'F').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def GArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'G').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def HArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'H').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def IArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'I').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def JArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'J').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def KArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'K').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def LArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'L').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def MArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'M').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def NArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'N').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def OArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'O').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def PArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'P').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def QArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'Q').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def RArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'R').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def SArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'S').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def TArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'T').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def UArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'U').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def VArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'V').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def WArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'W').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def XArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'X').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def YArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'Y').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)
def ZArtist(request):
	Perupa = perupa.object.filter(Kategori='Pelukis', Panggilan__startswith= 'Z').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/index.html', context)

#filtering patung --------------
def ASculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'A').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def BSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'B').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def CSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'C').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def DSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'D').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def ESculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'E').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def FSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'F').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def GSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'G').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def HSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'H').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def ISculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'I').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def JSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'J').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def KSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'K').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def LSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'L').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def MSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'M').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def NSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'N').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def OSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'O').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def PSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'P').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def QSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'Q').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def RSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'R').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def SSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'S').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def TSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'T').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def USculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'U').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def VSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'V').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def WSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'W').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def XSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'X').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def YSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'Y').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)
def ZSculptor(request):
	Perupa = perupa.object.filter(Kategori='Pematung', Panggilan__startswith= 'Z').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexpatung.html', context)

#filtering kriya --------------
def ACraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'A').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def BCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'B').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def CCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'C').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def DCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'D').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def ECraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'E').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def FCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'F').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def GCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'G').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def HCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'H').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def ICraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'I').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def JCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'J').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def KCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'K').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def LCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'L').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def MCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'M').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def NCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'N').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def OCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'O').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def PCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'P').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def QCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'Q').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def RCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'R').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def SCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'S').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def TCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'T').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def UCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'U').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def VCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'V').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def WCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'W').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def XCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'X').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def YCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'Y').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)
def ZCraft(request):
	Perupa = perupa.object.filter(Kategori='Pengrajin', Panggilan__startswith= 'Z').order_by('Panggilan')
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
		"perupa": Perupa,
		"page_request_var": Page_request_var
	}

	return render(request, 'artists/indexkriya.html', context)



# Karya----------------------------------------------------------------------------------------------------------
def Artlist(request):
	Karya = karya.object.all().filter(Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def Paintinglist(request):
	Karya = karya.object.all().filter(Jenis='Lukisan', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/lukisan.html', context)

def Statuelist(request):
	Karya = karya.object.all().filter(Jenis='Patung', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/patung.html', context)

def Craftlist(request):
	Karya = karya.object.all().filter(Jenis='Kriya', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/kriya.html', context)

#Filtering tema ------------------------------------------------------------------------------------------------

def Potraitlist(request):
	Karya = karya.object.all().filter(Kategori='Potret dan Sensualitas', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def Naturelist(request):
	Karya = karya.object.all().filter(Kategori='Alam dan Benda', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def Heroeslist(request):
	Karya = karya.object.all().filter(Kategori='Perjuangan dan Potret Para Pejuang', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def traditionlist(request):
	Karya = karya.object.all().filter(Kategori='Tradisi/Budaya/Mitologi/Keseharian', Naked_Material=False).order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def landscapelist(request):
	Karya = karya.object.all().filter(Kategori='Pemandangan Alam dan Kota').order_by('Kategori').distinct()
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

	return render(request, 'art/index.html', context)

def nudelist(request):
    Karya = karya.object.all().filter(Naked_Material=True).order_by('Kategori').distinct()
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

    return render(request, 'art/index.html', context)

def Artdetail(request, karya_id):
	try:
		Karya = karya.object.get(pk=karya_id)
	except Perupa.DoesNotExist:
		raise Http404('Data karya Belum Tersedia')

	context = {
		"Karya": Karya,
	}

	return render(request, 'art/detail.html', context)


# news----------------------------------------------------------------------------------------------------
def Newslist(request):
	Berita = News.object.all()[:1]
	return render(request, 'news/index.html', {'Berita': Berita})



# palace----------------------------------------------------------------------------------------------------
def PalaceBogor(request):
	return render(request, 'palace/istanabogor.html')

def PalaceNegara(request):
	return render(request, 'palace/istananegara.html')

def PalaceCipanas(request):
	return render(request, 'palace/istanacipanas.html')

def PalaceMerdeka(request):
	return render(request, 'palace/istanamerdeka.html')

def PalaceTampakSiring(request):
	return render(request, 'palace/istanatampaksiring.html')

def PalaceYogya(request):
	return render(request, 'palace/istanayogyakarta.html')


