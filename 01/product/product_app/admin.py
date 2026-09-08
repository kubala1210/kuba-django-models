from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "in_stock", "available_until")
    list_filter = ("in_stock",)
    search_fields = ("name",)


# Register your models here.
