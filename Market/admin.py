# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.forms import TextInput, Textarea
from django.db import models
from django.contrib.admin import SimpleListFilter
from django.db.models import Q
from django.contrib.admin import AdminSite

from .models import *
from django.http import HttpResponse, HttpResponseRedirect
import json
import requests

class ShopAdmin(admin.ModelAdmin):
    # fields = ('first_name, last_name', 'essay1', 'essay2')
    list_display = ( 'name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'getValue', 'manifest')

class LineAdmin(admin.ModelAdmin):
    list_display = ('name', 'getValue')

admin.site.register(Shop, ShopAdmin)
admin.site.register(LineItem, LineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
