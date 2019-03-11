from django.shortcuts import render, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from singgasanaseni.models import perupa, karya, berita, HomeSlide
from chsites.models import News


#Slider
def chindex(request):
    Berita = berita.object.all().order_by("-Tanggal")[:4]
    Slide = HomeSlide.objects.all()

    context = {
        "Berita": Berita,
        "Slide": Slide
    }
    return render (request, "chhome/chindex.html", context)

def chaboutus(request):
    return render (request, "chhome/aboutus.html")


# Perupa-----------------------------------------------------------------------------------------------
def chArtArtist(request):
	Perupa = perupa.object.all().order_by('Panggilan')
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

	return render(request, 'artist/indexlukisan.html', context)


def chPainterArtist(request):
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

	return render(request, 'artist/index.html', context)

def chSculptorlist(request):
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

	return render(request, 'artist/indexpatung.html', context)

def chCraftmanlist(request):
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

	return render(request, 'artist/indexkriya.html', context)

def chArtistsdetail(request, perupa_id):
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

	return render(request, 'artist/detail.html', context)

#filtering perupa --------------
def chAArtist(request):
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

	return render(request, 'artist/index.html', context)
def chBArtist(request):
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

	return render(request, 'artist/index.html', context)
def chCArtist(request):
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

	return render(request, 'artist/index.html', context)
def chDArtist(request):
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

	return render(request, 'artist/index.html', context)
def chEArtist(request):
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

	return render(request, 'artist/index.html', context)
def chFArtist(request):
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

	return render(request, 'artist/index.html', context)
def chGArtist(request):
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

	return render(request, 'artist/index.html', context)
def chHArtist(request):
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

	return render(request, 'artist/index.html', context)
def chIArtist(request):
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

	return render(request, 'artist/index.html', context)
def chJArtist(request):
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

	return render(request, 'artist/index.html', context)
def chKArtist(request):
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

	return render(request, 'artist/index.html', context)
def chLArtist(request):
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

	return render(request, 'artist/index.html', context)
def chMArtist(request):
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

	return render(request, 'artist/index.html', context)
def chNArtist(request):
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

	return render(request, 'artist/index.html', context)
def chOArtist(request):
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

	return render(request, 'artist/index.html', context)
def chPArtist(request):
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

	return render(request, 'artist/index.html', context)
def chQArtist(request):
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

	return render(request, 'artist/index.html', context)
def chRArtist(request):
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

	return render(request, 'artist/index.html', context)
def chSArtist(request):
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

	return render(request, 'artist/index.html', context)
def chTArtist(request):
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

	return render(request, 'artist/index.html', context)
def chUArtist(request):
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

	return render(request, 'artist/index.html', context)
def chVArtist(request):
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

	return render(request, 'artist/index.html', context)
def chWArtist(request):
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

	return render(request, 'artist/index.html', context)
def chXArtist(request):
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

	return render(request, 'artist/index.html', context)
def chYArtist(request):
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

	return render(request, 'artist/index.html', context)
def chZArtist(request):
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

	return render(request, 'artist/index.html', context)

#filtering patung --------------
def chASculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chBSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chCSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chDSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chESculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chFSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chGSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chHSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chISculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chJSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chKSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chLSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chMSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chNSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chOSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chPSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chQSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chRSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chSSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chTSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chUSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chVSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chWSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chXSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chYSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)
def chZSculptor(request):
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

	return render(request, 'artist/indexpatung.html', context)

#filtering kriya --------------
def chACraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chBCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chCCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chDCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chECraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chFCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chGCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chHCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chICraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chJCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chKCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chLCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chMCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chNCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chOCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chPCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chQCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chRCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chSCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chTCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chUCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chVCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chWCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chXCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chYCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)
def chZCraft(request):
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

	return render(request, 'artist/indexkriya.html', context)



# Karya----------------------------------------------------------------------------------------------------------
def chArtlist(request):
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

	return render(request, 'chart/index.html', context)

def chPaintinglist(request):
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

	return render(request, 'chart/lukisan.html', context)

def chStatuelist(request):
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

	return render(request, 'chart/patung.html', context)

def chCraftlist(request):
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

	return render(request, 'chart/kriya.html', context)

#Filtering tema ------------------------------------------------------------------------------------------------

def chPotraitlist(request):
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

	return render(request, 'chart/index.html', context)

def chNaturelist(request):
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

	return render(request, 'chart/index.html', context)

def chHeroeslist(request):
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

	return render(request, 'chart/index.html', context)

def chtraditionlist(request):
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

	return render(request, 'chart/index.html', context)

def chlandscapelist(request):
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

	return render(request, 'chart/index.html', context)

def chnudelist(request):
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

    return render(request, 'chart/index.html', context)

def chArtdetail(request, karya_id):
	try:
		Karya = karya.object.get(pk=karya_id)
	except karya.DoesNotExist:
		raise Http404('Data karya Belum Tersedia')

	context = {
		"Karya": Karya,
	}

	return render(request, 'chart/detail.html', context)


# news----------------------------------------------------------------------------------------------------
def chNewslist(request):
	Berita = News.object.all()
	return render(request, 'chnews/index.html', {'Berita': Berita})



# palace----------------------------------------------------------------------------------------------------
def chPalaceBogor(request):
	return render(request, 'chpalace/istanabogor.html')

def chPalaceNegara(request):
	return render(request, 'chpalace/istananegara.html')

def chPalaceCipanas(request):
	return render(request, 'chpalace/istanacipanas.html')

def chPalaceMerdeka(request):
	return render(request, 'chpalace/istanamerdeka.html')

def chPalaceTampakSiring(request):
	return render(request, 'chpalace/istanatampaksiring.html')

def chPalaceYogya(request):
	return render(request, 'chpalace/istanayogyakarta.html')


