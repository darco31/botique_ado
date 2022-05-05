from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    The below sets the display in admin to include the headers
    outlined below
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    The below sets the display in admin to include the headers
    outlined below
    """
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
