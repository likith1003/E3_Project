from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CartItems(models.Model):
    cart_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    inst = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name