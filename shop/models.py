from django.db import models

# Create your models here.

class ProdCategory(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="prodCategory"
        verbose_name_plural="prodCategories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    categories=models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="shop", null=True, blank=True)
    price=models.FloatField()
    stock=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
