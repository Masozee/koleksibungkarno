from django.contrib import admin
from .models import *

# Register your models here.
class KaryaAdmin (admin.ModelAdmin):
    list_display = ['No_Index', 'Judul', 'Perupa', 'Dimensi', 'Material', 'Tahun_Pembuatan', 'Lokasi_Lukisan']
    list_filter = ("Material", "Lokasi_Lukisan")
    search_fields = ['No_Index', 'Judul', 'Perupa_perupa__Nama', 'Dimensi', 'Material', 'Tahun_Pembuatan', 'Lokasi_Lukisan__istana']
    list_per_page = 25

admin.site.register(karya,KaryaAdmin)


# perupa admin
class PerupaAdmin (admin.ModelAdmin):
    list_display = ['Nama', 'Panggilan', 'Alamat', 'Tanggal_Lahir']
    list_filter = ()
    search_fields = ['Nama', 'panggilan', 'Alamat', 'Tanggal_Lahir']
    list_per_page = 25

admin.site.register(perupa, PerupaAdmin)


#istana
class IstanaAdmin (admin.ModelAdmin):
    list_display = ['Nama', 'Alamat']
    list_filter = ()
    search_fields = ['Nama', 'Alamat']
    list_per_page = 25

admin.site.register(istana,IstanaAdmin)

#event
class AcaraAdmin (admin.ModelAdmin):
    list_display = ['Nama', 'Lokasi', 'Mulai', 'Akhir']
    list_filter = ()
    search_fields = ['Nama', 'Lokasi', 'Mulai', 'Akhir']
    list_per_page = 25

admin.site.register(acara,AcaraAdmin)

#event
class KuratorAdmin (admin.ModelAdmin):
    list_display = ['Nama']
    list_filter = ()
    search_fields = ['Nama']
    list_per_page = 25

admin.site.register(kurator,KuratorAdmin)