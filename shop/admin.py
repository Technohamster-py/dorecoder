from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent_category']
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ['parent_category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}
# Register your models here.
