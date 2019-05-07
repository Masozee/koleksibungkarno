from django.contrib import admin
from .models import *

# Register your models here.
class KaryaAdmin (admin.ModelAdmin):
    ordering = ['Judul']
    list_display = ['No_Index', 'Judul', 'Perupa', 'Dimensi', 'Material','Kategori', 'Tahun_Pembuatan', 'Lokasi_Lukisan', 'Naked_Material', 'tag_list']
    list_filter = ("Material", "Lokasi_Lukisan")
    search_fields = ['No_Index', 'Judul', 'Dimensi', 'Material', 'Tahun_Pembuatan']
    list_per_page = 25

    def get_queryset(self, request):
        return super(KaryaAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(karya,KaryaAdmin)


# perupa admin
class PerupaAdmin (admin.ModelAdmin):
    ordering = ['Panggilan']
    list_display = ['Panggilan','Nama', 'Kategori', 'Tanggal_Lahir', 'Tanggal_Wafat', 'Upload_date']
    list_filter = ()
    search_fields = ['Nama', 'Panggilan', 'Kategori', ]
    list_per_page = 25

admin.site.register(perupa, PerupaAdmin)


#event
class BeritaAdmin (admin.ModelAdmin):
    list_display = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Gambar']
    list_filter = ()
    search_fields = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Isiberita', 'Gambar']
    list_per_page = 25

admin.site.register(berita,BeritaAdmin)

admin.site.register(HomeSlide)


class InquiryAdmin (admin.ModelAdmin):
    list_display = ['Email', 'Judul', 'Nama']
    list_filter = ()
    search_fields = ['Email', 'Judul', 'Nama']
    list_per_page = 25

admin.site.register(Inquiry,InquiryAdmin)
