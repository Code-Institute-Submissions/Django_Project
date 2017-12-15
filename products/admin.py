from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','description','image','stock','created','updated','available',]
    list_filter = ['created','updated','available','category']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


