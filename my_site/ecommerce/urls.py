from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.ProductDetailView.as_view(), name="detail"),
    path("checkout", views.checkout, name="checkout"),
    path("order_confirmed", views.order_confirmed, name="order_confirmed")
]