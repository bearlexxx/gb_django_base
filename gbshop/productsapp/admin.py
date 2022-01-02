from django.contrib import admin

from productsapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)