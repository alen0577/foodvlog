from django.db import models
from shop.models import *


# Create your models here.

class Cartlist(models.Model):
    cart_id = models.CharField(max_length=200, unique=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class Items(models.Model):
    product = models.ForeignKey(Prod, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product

    def total(self):
        return self.product.price * self.quantity

