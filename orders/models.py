from django.db import models
from django.http.response import HttpResponse
from .utils import generate_code, validation_six_digits, validation_stock
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(blank=True)
    listing_price = models.FloatField(blank=True)
    stock = models.IntegerField(validators={validation_stock})
    short_description = models.TextField(max_length=150)
    product_number = models.PositiveIntegerField(unique=True, blank=True, validators=[validation_six_digits])




    def __str__(self):
        return str(self.title)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    title = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=12, unique=True, blank=True)

    
    def save(self, *args, **kwargs):
        self.total = self.product.price * self.amount
        self.product.stock -= self.amount
        if self.product.stock >= 0:
            self.product.save()
        else:
            raise ValidationError(
                _('%(value)s% Has not enough stock'),
                params={'value':self.product}
            )  
        if self.order_number == "":
            self.order_number = generate_code()
        if self.title == "":
            self.title = self.product.title
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.order_number} order"