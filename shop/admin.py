from django.contrib import admin
from shop.models import Product, Contact, Order, OrderUpdate

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
