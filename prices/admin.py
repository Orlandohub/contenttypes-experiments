from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from prices.models import RentPriceTable, SellingPrice
from products.models import Product


class RentPriceTableAdmin(admin.ModelAdmin):
    models = RentPriceTable

admin.site.register(RentPriceTable, RentPriceTableAdmin)
