from django.shortcuts import render


from singgasanaseni.models import berita
from homepage.models import HomeSlide

# Create your views here.
def index(request):
    Berita = berita.object.all().order_by("Upload_date")[:4]
    Slide = HomeSlide.objects.all()

    context = {
        "Berita": Berita,
        "Slide": Slide
    }
    return render (request, "index.html", context)


def tentangkami(request):
    return render (request, "tentangkami.html")

