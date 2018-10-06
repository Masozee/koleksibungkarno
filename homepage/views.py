from django.shortcuts import render,  Http404

# Create your views here.
def index(request):
    return render (request, "index.html")

def tentangkami(request):
    return render (request, "tentangkami.html")