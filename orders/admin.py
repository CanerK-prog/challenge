from django.contrib import admin
from orders.models import Order, Product
# Register your models here.


admin.site.register(Product)
admin.site.register(Order)