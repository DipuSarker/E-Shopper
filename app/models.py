from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    Availability = (
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock')
    )
    Condition = (
        ('New Version', 'New Version'),
        ('Old Version', 'Old Version'),
        ('Latest Version', 'Latest Version')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=False)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default='', null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    availability = models.CharField(max_length=100, choices=Availability, null=True)
    condition = models.CharField(max_length=100, choices=Condition, null=True)
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email


class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.product
