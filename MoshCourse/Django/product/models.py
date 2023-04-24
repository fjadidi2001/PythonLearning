from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=225)
    stock = models.IntegerField(max_length=2083)
    image_urls = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    des = models.CharField(max_length=255)
    dis = models.FloatField()
