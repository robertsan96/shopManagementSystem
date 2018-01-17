from django.contrib import admin
from .models import Category, Item
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'description', 'price',
                    'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
