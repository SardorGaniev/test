from django.contrib import admin
from .models import *

class Product_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'date')
    list_display_links = ('id', 'name', 'date')

admin.site.register(Product, Product_Admin)

class Stuff_Admin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'age', 'position', 'date')
    list_display_links = ('id', 'fullname', 'date')

admin.site.register(Stuff, Stuff_Admin)

class Form_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'select')
    list_display_links = ('id', 'name', 'phone', 'email', 'select')

admin.site.register(Contact, Form_admin)

