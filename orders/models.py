from django.db import models

from django.contrib.auth import get_user_model
from shop.models import Product
from django.db.models import F, Sum, FloatField

# Create your models here.

User=get_user_model()

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("price")*F("amount"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='orders'
        verbose_name='order'
        verbose_name_plural='orders'
        ordering=['id']

class OrderLine(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} unidades de {self.product.name}'
    
    class Meta:
        db_table='orderline'
        verbose_name='orderline'
        verbose_name_plural='orderslines'
        ordering=['id']