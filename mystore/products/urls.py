from django.urls import path, re_path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductList.as_view(), name="product_list"),
    re_path(r"(?P<pk>\d+)/$", views.ProductDetail.as_view(), name="detail"),
    path("update_item/", views.update_item, name="update_item"),
    path("cart/", views.CartList.as_view(), name="cart_list"),
    path("order/", views.order_save, name="order"),
    path("order_list/", views.OrderList.as_view(), name="order_list"),
    path("wishlist/", views.WishListView.as_view(), name="wishlist"),
    path("update_wishlist/", views.update_wishlist, name="update_wishlist"),
]
