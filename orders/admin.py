from django.contrib import admin
from .models import Payment, Order, OrderProduct
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment','user', 'quantity', 'product_price', 'ordered', 'product')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'city', 'order_total','tax', 'status', 'is_ordered']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    list_display_links = ('order_number', 'full_name', 'phone')
    inlines = [OrderProductInline]
    
admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
