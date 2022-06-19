from django.contrib import admin
from .models import *


# Register your models here.

class Catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, Catadmin)


class Proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img', 'available']
    list_editable = ['price', 'stock', 'img', 'available']


admin.site.register(Prod, Proadmin)
