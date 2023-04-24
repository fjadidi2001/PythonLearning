from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return HttpResponse("this is is")


def new(request):
    return HttpResponse("what is that?")

