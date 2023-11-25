from django.db import models


class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    order = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    customization = models.CharField(max_length=100)

class UserProduct(models.Model):
    name = models.CharField(max_length=100)
    organize = models.CharField(max_length=100)
    ph = models.CharField(max_length=15)
    mail = models.EmailField()
    orders = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    product_customization = models.CharField(max_length=100)
    product = models.CharField(max_length=100)


