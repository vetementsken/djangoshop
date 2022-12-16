from django.contrib import admin
from django.urls import path


from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('order-summary', OrderSummeryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('category/<str:slug>/', Post_By_Category.as_view(), name='category'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    ]