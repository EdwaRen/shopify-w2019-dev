from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^shop/$', views.shop_list),
    url(r'^product/$', views.product_list),
    url(r'^order/$', views.order_list),
    url(r'^line/$', views.line_list),

]
