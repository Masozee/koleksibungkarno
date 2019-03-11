from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import News

# Register your models here.
class NewsAdmin (admin.ModelAdmin):
    list_display = ['Date', 'Tittle', 'SubTittle', 'Source', 'Link', 'Image']
    list_filter = ()
    search_fields = ['Date', 'Tittle', 'SubTittle', 'Source', 'Link', 'Content', 'Image']
    list_per_page = 25

admin.site.register(News,NewsAdmin)