from django.contrib import admin

from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
