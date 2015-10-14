from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Product
from prices.models import RentPriceTable, SellingPrice

PRICE = ""


class RentPriceTableInline(GenericTabularInline):
    model = RentPriceTable
    extra = 1
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class SellingPriceInline(GenericTabularInline):
    model = SellingPrice
    extra = 1
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    model = Product
    if PRICE == "rent":
        inlines = (RentPriceTableInline,)
    else:
        inlines = (SellingPriceInline,)

admin.site.register(Product, ProductAdmin)
