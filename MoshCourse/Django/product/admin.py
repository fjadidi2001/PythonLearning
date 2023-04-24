from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    List_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    List = ('code', 'dis')


admin.site.register(Offer, OfferAdmin)