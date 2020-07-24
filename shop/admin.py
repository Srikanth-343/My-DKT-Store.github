from django.contrib import admin
from .models import  Product, Contact, Order,OrderUpdate
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','price','pub_date',]
    list_editable = ['price',]
    list_per_page = 50
admin.site.register(Product,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone',]
    list_per_page = 50
admin.site.register(Contact, ContactAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','email','items_json','amount',]
    list_per_page = 50
admin.site.register(Order, OrderAdmin)

class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ['order_id','update_id','update_desc','timestamp',]
    list_per_page = 50
admin.site.register(OrderUpdate, OrderUpdateAdmin)