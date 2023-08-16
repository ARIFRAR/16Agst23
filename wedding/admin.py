from django.contrib import admin
from .models import Wedding
from django.utils.html import format_html

# Register your models here.

class WeddingAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(obj.wedding_photo.url))

    thumbnail.short_description = 'Wedding Image'
    list_display = ('id', 'thumbnail', 'Paket', 'durasi_acara', 'Harga', 'Unggulan')
    list_filter = ('durasi_acara', 'Unggulan')
    list_editable = ('Unggulan',)
    search_fields = ('Paket', 'durasi_acara')

admin.site.register(Wedding, WeddingAdmin)

