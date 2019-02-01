from django.contrib import admin

from .models import News

# Register your models here.
class NewsAdmin (admin.ModelAdmin):
    list_display = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Gambar']
    list_filter = ()
    search_fields = ['Tanggal', 'Judul', 'Subjudul', 'Sumber', 'Link', 'Isiberita', 'Gambar']
    list_per_page = 25

admin.site.register(News,NewsAdmin)