from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(max_length=5000)
    description = models.TextField()

    def __str__(self):
        return self.name


class WishList(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_wishlist",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_cart",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_product"
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username + " " + self.product.name


class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_order",
        on_delete=models.CASCADE,
    )

    product = models.ManyToManyField(Product)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username
