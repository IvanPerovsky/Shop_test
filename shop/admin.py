from django.contrib import admin
from .models import Category, Product, Subcategory, Property


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Subcategory, SubcategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(Property, PropertyAdmin)