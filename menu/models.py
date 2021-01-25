# -*- encoding: utf-8 -*-
"""
This module create models for category.
"""

from __future__ import unicode_literals

import os
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


# class ItemManager(models.Manager):
#     """
#     Filter all objects for instance.
#     """
#     def filter_by_instance(self, instance):
#         content_type = ContentType.objects.get_for_model(instance.__class__)
#         obj_id = instance.id
#         qs = super(ItemManager, self).filter(content_type=content_type, object_id=obj_id, parent=None)
#         return qs


class Item(models.Model):
    """
    Stores a menu`s items for menu.
    """
    title = models.CharField(max_length=50, verbose_name="Назва пункту")
    used = models.BooleanField(verbose_name="Вживані", default=False)
    promotions = models.BooleanField(
        verbose_name="Знижені ціни", default=False)
    slug = models.SlugField(
        verbose_name="Ім`я категорії транслітом", unique=True, max_length=100)
    create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення")
    update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name="Belong model")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # objects = ItemManager()

    class Meta:
        """
        Change db_table name, verbose_name, verbose_name_plural
        """
        ordering = ['object_id', 'id']
        db_table = "items"
        verbose_name = "Пункти категорії"
        verbose_name_plural = "Пункти категорій"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.parent:
            self.slug = slugify("{} {} {}".format(self.title, self.parent.title, self.parent.id),
                                allow_unicode=True)
        self.slug = slugify("{} {} {}".format(self.title, self.content_object.title, self.object_id),
                            allow_unicode=True)
        super(Item, self).save(*args, **kwargs)

    def category(self):
        if self.content_type.model_class() == Category:
            return self.content_object
        elif self.parent.content_type.model_class() == Category:
            return self.parent.content_object
        else:
            return None

    # def content_type_object(self, obj):
    #     type_objects = obj.content_type.get_object_for_this_type(
    #         id=obj.object_id)
    #     return type_objects

    # content_type_object.short_description = 'Name'

    # def has_parent_children(self):
    #     instance = self
    #     return hasattr(instance.parent, 'children')

    # def get_all_products(self):
    #     from product.models import Product
    #     products = Product.objects.filter(Q(item__in=self.children()) | Q(item=self)).distinct()
    #     return products

    # def get_absolute_url(self):
    #     return reverse('product:product_list', kwargs={
    #         'slug': self.slug})


def upload_location(instance, filename):
    path = 'upload/category'
    return os.path.join(path, str(instance.title), str(filename))


class Category(models.Model):
    """
    Stores a menu for menu.
    """
    title = models.CharField(max_length=50, verbose_name="Назва категорії")
    used = models.BooleanField(verbose_name="Вживані", default=False)
    promotions = models.BooleanField(
        verbose_name="Знижені ціни", default=False)
    slug = models.SlugField(
        verbose_name="Ім`я категорії транслітом", unique=True)
    create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення")
    update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    image = models.ImageField(verbose_name="Картинка", upload_to=upload_location, width_field="width_field",
                              height_field="height_field", blank=True, null=True,
                              help_text="Картинка категории")

    width_field = models.IntegerField(
        default=0, verbose_name="Ширина картинки в пікселях")
    height_field = models.IntegerField(
        default=0, verbose_name="Висота картинки в пікселях")

    items = GenericRelation(Item)

    class Meta:
        """
        Change db_table name, verbose_name, verbose_name_plural
        """
        ordering = ['id', ]
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def get_absolute_url(self):
        return reverse('menu:items_list', kwargs={
            'slug': self.slug})

    def natural_key(self):
        return self.slug
