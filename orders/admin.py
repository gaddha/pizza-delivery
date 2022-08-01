from django.contrib import admin
from orders.models import order
# Register your models here.
@admin.register(order)
class orderadmin(admin.ModelAdmin):
  list_display = ['size','order_status','quantity','created_at']
  list_filter = ['created_at','order_status','size']
