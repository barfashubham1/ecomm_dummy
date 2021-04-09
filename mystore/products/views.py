from django.shortcuts import render

from .models import Product, Cart, Order, WishList
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Sum
from django.db.models import FloatField


class ProductList(generic.ListView):
    model = Product
    template_name = "products/product_list.html"


class CartList(generic.ListView):
    model = Cart
    context_object_name = "cart_list"
    template_name = "products/cart_list.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["cart_qty"] = Cart.objects.filter(user=user).aggregate(Sum("quantity"))
        context["cart_of_user"] = Cart.objects.filter(user=user)
        total = 0
        for val in context.get("cart_of_user"):
            total += val.quantity * val.product.price
        context["cart_total"] = total
        return context


class ProductDetail(generic.DetailView):
    model = Product


class OrderList(generic.ListView):
    model = Order
    template_name = "products/order_list.html"


class WishListView(generic.ListView):
    model = WishList
    context_object_name = "wish_list"
    template_name = "products/wishlist.html"


@login_required
def update_item(request):

    data = json.loads(request.body)
    product_id = data.get("productId")
    user = request.user
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(product=product, user=user)
        if cart.quantity >= 1:
            cart.quantity = cart.quantity + 1
            cart.save()
    except Cart.DoesNotExist:
        cart = Cart(user=user, product=product, quantity=1)
        cart.save()

    return JsonResponse("item was added ", safe=False)


@login_required
def order_save(request):
    user = request.user
    user_cart = list(Cart.objects.filter(user=user))
    total = 0
    for val in user_cart:
        total += val.quantity * val.product.price
    order_total= total
    order = Order.objects.create(user=user, order_total=total)

    for item in user_cart:
        order.product.add(item.product)
    order.save()
    Cart.objects.filter(user=user).delete()

    return JsonResponse("Order Placed.. ", safe=False)


@login_required
def update_wishlist(request):

    data = json.loads(request.body)
    product_id = data.get("productId")
    user = request.user
    product = Product.objects.get(id=product_id)
    try:
        wishlist = WishList.objects.get(product=product, user=user)
    except WishList.DoesNotExist:
        wishlist = WishList(user=user, product=product)
        wishlist.save()
    return JsonResponse("Order Placed.. ", safe=False)
