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

	return render(request, 'perupa/indexpatung.html', context)

def Pengrajinlist(request):
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

#filtering patung --------------
def APatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def BPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def CPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def DPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def EPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def FPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def GPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def HPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def IPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def JPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def KPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def LPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def MPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def NPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def OPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def PPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def QPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def RPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def SPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def TPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def UPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def VPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def WPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def XPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def YPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)
def ZPatung(request):
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

	return render(request, 'perupa/indexpatung.html', context)

#filtering kriya --------------
def AKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def BKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def CKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def DKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def EKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def FKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def GKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def HKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def IKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def JKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def KKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def LKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def Mkriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def NKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def OKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def PKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def QKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def RKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def SKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def TKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def UKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def VKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def WKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def XKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def YKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)
def ZKriya(request):
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

	return render(request, 'perupa/indexkriya.html', context)



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


# news----------------------------------------------------------------------------------------------------
def Beritalist(request):
	Berita = berita.object.all()
	return render(request, 'berita/index.html', {'Berita': Berita})



# palace----------------------------------------------------------------------------------------------------
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


