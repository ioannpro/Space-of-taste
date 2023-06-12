from django.contrib import admin

from .models import *

class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'options')
    list_display_links = ('id', 'name')


admin.site.register(Dish,DishAdmin,)