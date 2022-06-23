from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'description', 'image', 'date_added')
    list_filter = ('category',)
    list_display_links = ('name', 'price', 'description')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
