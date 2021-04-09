from django.contrib import admin
from .models import Product, WishList, Cart, Order

class AdminOrder(admin.ModelAdmin):
    readonly_fields = ('order_date',)

admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Order,AdminOrder)
