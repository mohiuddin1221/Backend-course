from django.contrib import admin
from .models import(
    Category,
    Product,
    Order
)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['category_name','slug','create_at','update_at']
    prepopulated_fields = {'slug': ('category_name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['product_name','slug','product_Description','price','category','image','create_at','update_at']
    prepopulated_fields = {'slug': ('product_name',)}
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ['customer_name','customer_email','product','quantity','create_at']
    