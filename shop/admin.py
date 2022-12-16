from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order, Category


class ProductAdmin(admin.ModelAdmin):

    save_as = True  # после добавления, текст остается
    save_on_top = True  # кнопка сохранения сверху


admin.site.register(Item, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)
