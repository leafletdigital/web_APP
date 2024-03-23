from django.contrib import admin
from Products.models import product
class ProductAdmin(admin.ModelAdmin):
    list_display=("product_title","product_feature","product_cost","product_link","product_img")
# Register your models here.
admin.site.register(product,ProductAdmin)