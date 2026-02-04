from django.contrib import admin
from.models import Product

# Register product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = {"name", "description", "price", "amount"}


