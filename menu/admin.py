from django.contrib import admin
from django.contrib.contenttypes.admin import (
    GenericStackedInline, GenericTabularInline)
from menu.models import (Category, Item)


class ItemInLine(GenericStackedInline):
    model = Item
    fieldsets = [
        # (None, {'fields': ['title', 'used', 'promotions', 'slug']}),
        ('Скриті дані', {
            'classes': ('collapse',),
            'fields': ('title', 'used', 'promotions', 'slug'),
        }),
    ]
    extra = 1
    verbose_name = 'Пункт категорії'
    verbose_name_plural = "Пункти категорії"
    readonly_fields = ['slug', ]


class ItemsInLine(GenericTabularInline):
    model = Item
    extra = 2
    verbose_name = 'Підпункт'
    verbose_name_plural = "Підпункти"
    readonly_fields = ['slug', 'parent']

    # radio_fields = {'parent': admin.VERTICAL, }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fieldsets = [
        (None, {'fields': ['title',  'used', 'promotions',
                           'slug', 'image', 'create', 'update']})
    ]
    list_display = ['title', 'create', 'slug', 'used', 'promotions', 'id']
    readonly_fields = ['slug', 'create', 'update']
    inlines = [ItemInLine]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    fieldsets = [
        (None, {'fields': ['title', 'used', 'promotions', 'content_type', 'object_id',
                           'parent', 'slug', 'create', 'update', 'pk']})
    ]
    list_display = ['title', 'used', 'promotions',
                    'content_object',  'parent', 'id']
    readonly_fields = ['slug', 'create', 'update', 'pk']
    list_select_related = ('parent', )

    search_fields = ['title', ]
    list_per_page = 10

    inlines = [ItemsInLine]
