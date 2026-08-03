from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("place-order/", views.place_order, name="place_order"),

    path("payment/<int:order_id>/", views.payment, name="payment"),
    path("payment-success/<int:order_id>/", views.payment_success, name="payment_success"),

    path("success/<int:order_id>/", views.order_success, name="order_success"),

    path("my-orders/", views.my_orders, name="my_orders"),

    path(
    "invoice/<int:order_id>/",
    views.invoice,
    name="invoice"
),
]