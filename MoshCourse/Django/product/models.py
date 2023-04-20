from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField()
    stock = models.IntegerField()
    image_urls = models.CharField(max_length=2083)



