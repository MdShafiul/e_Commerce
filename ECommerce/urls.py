from django.urls import path

from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    OrderTracking,
    order_not_received,
    order_received,
    RequestRefundView
)

app_name = 'ECommerce'

urlpatterns = [
path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('track-your-order/', OrderTracking.as_view(), name='track-your-order'),
    path('order-not-received/', order_not_received, name='order-not-received'),
    path('order-received/', order_received, name='order-received'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]