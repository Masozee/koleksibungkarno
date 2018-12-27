from django.shortcuts import render


from singgasanaseni.models import berita

# Create your views here.
def index(request):
    Berita = berita.object.all().order_by("Upload_date")[:4]
    return render (request, "index.html", {'Berita': Berita})


def tentangkami(request):
    return render (request, "tentangkami.html")