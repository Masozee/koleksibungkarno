from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse

from singgasanaseni.models import *

class KaryaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return karya.object.all()

class PerupaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return perupa.object.all()

class BeritaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return berita.object.all()

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['istana-bogor', 'istana-cipanas', 'istana-merdeka', 'istana-tampaksiring', 'istana-yogyakarta', 'tentang-kami']

    def location(self, item):
        return reverse(item)


