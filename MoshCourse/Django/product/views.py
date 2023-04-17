from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("this is is")


def new(request):
    return HttpResponse("what is that?")
