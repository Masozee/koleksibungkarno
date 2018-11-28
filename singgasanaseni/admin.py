from django.contrib import admin
from .models import *

# Register your models here.
class KaryaAdmin (admin.ModelAdmin):
    list_display = ['No_Index', 'Judul', 'Perupa', 'Dimensi', 'Material','Kategori', 'Tahun_Pembuatan', 'Lokasi_Lukisan']
    list_filter = ("Material", "Lokasi_Lukisan")
    search_fields = ['No_Index', 'Judul', 'Perupa_perupa__Nama', 'Dimensi', 'Material', 'Tahun_Pembuatan', 'Lokasi_Lukisan__istana']
    list_per_page = 25

admin.site.register(karya,KaryaAdmin)


# perupa admin
class PerupaAdmin (admin.ModelAdmin):
    list_display = ['Nama', 'Panggilan', 'Kategori', 'Tanggal_Lahir']
    list_filter = ()
    search_fields = ['Nama', 'panggilan', 'Kategori', 'Tanggal_Lahir']
    list_per_page = 25

admin.site.register(perupa, PerupaAdmin)


#event
class BeritaAdmin (admin.ModelAdmin):
    list_display = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Gambar']
    list_filter = ()
    search_fields = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Isiberita', 'Gambar']
    list_per_page = 25

admin.site.register(berita,BeritaAdmin)

