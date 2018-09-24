# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return (self.name)

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    value = models.IntegerField(blank=True, null=True, default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return (self.name)

class Order(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (self.name)

    def getValue(self):
        list_lines = LineItem.objects.filter(order=self)
        value = 0
        for i in list_lines:
            value += i.getValue()
        return value

    def manifest(self):
        list_lines = LineItem.objects.filter(order=self)
        return [i.product.name + " - " + i.name for i in list_lines]

class LineItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='%(class)s_order_created', blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True, default='')

    def save(self, *args, **kwargs):
        super(LineItem, self).save(*args, **kwargs)

    def getValue(self):
        return self.product.value

    def __str__(self):
        return (self.name)

# Create your models here.
