from django.contrib import admin
from .models import Orders, OrderDetails

admin.site.register(Orders)
admin.site.register(OrderDetails)