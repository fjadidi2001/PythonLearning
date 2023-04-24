from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    List_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
