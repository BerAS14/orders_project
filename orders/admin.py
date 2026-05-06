from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'name', 'status', 'created_at', 'ready_date']
    list_filter = ['status', 'order_type']
    search_fields = ['order_number', 'name']
    readonly_fields = ['order_number', 'created_at']