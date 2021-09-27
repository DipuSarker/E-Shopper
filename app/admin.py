from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Sub_Category)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Brand)
admin.site.register(Order)

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'date']
admin.site.register(Product, AdminProduct)