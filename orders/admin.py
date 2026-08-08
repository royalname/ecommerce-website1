from django.contrib import admin
from django.utils import timezone
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "full_name", "total_amount", "status", "payment_method", "payment_status", "stock_reduced", "created_at",)
    list_filter = ("status", "payment_method", "payment_status", "stock_reduced", "created_at",)
    search_fields = ("user__username", "full_name", "phone", "email",)
    readonly_fields = ("created_at",)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = ("id", "order", "product", "quantity", "price",)
    list_filter = ("order", "product",)
    search_fields = ("order__id", "product__name",)

