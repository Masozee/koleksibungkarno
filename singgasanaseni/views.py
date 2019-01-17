from django.shortcuts import render, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from singgasanaseni.models import perupa, karya, berita


# Perupa-----------------------------------------------------------------------------------------------
def PerupaList(request):
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

	return render(request, 'perupa/index.html', context)

def Pematunglist(request):
	Pematung = perupa.object.filter(Kategori='Pematung').order_by('Panggilan')
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
		"pematung": Pematung,
		"page_request_var": Page_request_var
	}

	return render(request, 'perupa/indexpatung.html', context)

def Pengrajinlist(request):
	Pengrajin = perupa.object.filter(Kategori='Pengrajin').order_by('Panggilan')
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
		"pengrajin": Pengrajin,
		"page_request_var": Page_request_var
	}

	return render(request, 'perupa/indexkriya.html', context)

def Perupadetail(request, perupa_id):
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

	return render(request, 'perupa/detail.html', context)

#filtering perupa --------------
def AList(request):
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

	return render(request, 'perupa/index.html', context)
def BList(request):
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

	return render(request, 'perupa/index.html', context)
def CList(request):
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

	return render(request, 'perupa/index.html', context)
def DList(request):
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

	return render(request, 'perupa/index.html', context)
def EList(request):
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

	return render(request, 'perupa/index.html', context)
def FList(request):
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

	return render(request, 'perupa/index.html', context)
def GList(request):
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

	return render(request, 'perupa/index.html', context)
def HList(request):
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

	return render(request, 'perupa/index.html', context)
def IList(request):
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

	return render(request, 'perupa/index.html', context)
def JList(request):
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

	return render(request, 'perupa/index.html', context)
def KList(request):
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

	return render(request, 'perupa/index.html', context)
def LList(request):
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

	return render(request, 'perupa/index.html', context)
def MList(request):
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

	return render(request, 'perupa/index.html', context)
def NList(request):
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

	return render(request, 'perupa/index.html', context)
def OList(request):
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

	return render(request, 'perupa/index.html', context)
def PList(request):
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

	return render(request, 'perupa/index.html', context)
def QList(request):
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

	return render(request, 'perupa/index.html', context)
def RList(request):
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

	return render(request, 'perupa/index.html', context)
def SList(request):
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

	return render(request, 'perupa/index.html', context)
def TList(request):
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

	return render(request, 'perupa/index.html', context)
def UList(request):
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

	return render(request, 'perupa/index.html', context)
def VList(request):
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

	return render(request, 'perupa/index.html', context)
def WList(request):
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

	return render(request, 'perupa/index.html', context)
def XList(request):
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

	return render(request, 'perupa/index.html', context)
def YList(request):
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

	return render(request, 'perupa/index.html', context)
def ZList(request):
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

	return render(request, 'perupa/index.html', context)








# Karya----------------------------------------------------------------------------------------------------------
def karyalist(request):
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

	return render(request, 'karya/index.html', context)

def lukisanlist(request):
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

	return render(request, 'karya/lukisan.html', context)

def Patunglist(request):
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

	return render(request, 'karya/patung.html', context)

def kriyalist(request):
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

	return render(request, 'karya/kriya.html', context)

#Filtering tema ------------------------------------------------------------------------------------------------

def potretlist(request):
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

	return render(request, 'karya/index.html', context)

def alamlist(request):
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

	return render(request, 'karya/index.html', context)

def juanglist(request):
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

	return render(request, 'karya/index.html', context)

def tradisilist(request):
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

	return render(request, 'karya/index.html', context)

def alamkotalist(request):
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

	return render(request, 'karya/index.html', context)

def karyadetail(request, karya_id):
	try:
		Karya = karya.object.get(pk=karya_id)
	except Perupa.DoesNotExist:
		raise Http404('Data karya Belum Tersedia')

	context = {
		"Karya": Karya,
	}

	return render(request, 'karya/detail.html', context)


# berita----------------------------------------------------------------------------------------------------
def Beritalist(request):
	Berita = berita.object.all()
	return render(request, 'berita/index.html', {'Berita': Berita})



# istana----------------------------------------------------------------------------------------------------
def IstanaBogor(request):
	return render(request, 'istana/istanabogor.html')

def IstanaNegara(request):
	return render(request, 'istana/istananegara.html')

def IstanaCipanas(request):
	return render(request, 'istana/istanacipanas.html')

def IstanaMerdeka(request):
	return render(request, 'istana/istanamerdeka.html')

def IstanaTampakSiring(request):
	return render(request, 'istana/istanatampaksiring.html')

def IstanaYogya(request):
	return render(request, 'istana/istanayogyakarta.html')


