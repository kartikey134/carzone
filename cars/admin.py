from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.carPhoto.url))

    thumbnail.short_description = 'Car Image';
    list_display = ('id', 'thumbnail', 'carTitle', 'city', 'color', 'year', 'bodyStyle', 'fuelType', 'isFeatured')
    list_display_links = ('id', 'thumbnail', 'carTitle')
    list_editable = ('isFeatured',)

    search_fields = ('id', 'carTitle', 'city', 'model', 'bodyStyle', 'fuelType')
    list_filter = ('city', 'model', 'bodyStyle', 'fuelType')

admin.site.register(Car, CarAdmin)
