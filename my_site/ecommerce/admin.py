from django.contrib import admin
from .models import Product, Category, Order

# Register your models here.
admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "MyShop"
admin.site.index_title = "Manage MyShop Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "discounted_price", "category", "description")
    search_fields = ["title"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)