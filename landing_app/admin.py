from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'price_per_kg',
        'price_per_100g',
        'description',
        'get_html_image',
        'is_published',
        'date_added',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'category',
    )
    list_display_links = (
        'name',
        'price',
        'description',
    )
    fields = (
        'name',
        'category',
        'description',
        'price',
        'price_per_kg',
        'price_per_100g',
        'image',
        'date_added',
    )
    readonly_fields = (
        'date_added',
    )

    def get_html_image(self, object):
        return mark_safe(f'<img src="{object.image.url}" width=50')

    get_html_image.short_description = 'фото'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = '"Особый случай"'
admin.site.site_header = 'Администрирование приложения "Особый случай"'
