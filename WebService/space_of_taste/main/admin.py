from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','icons')

class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'options','categori')
    list_display_links = ('id', 'name')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Dish,DishAdmin,)