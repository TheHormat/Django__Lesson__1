from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return HttpResponse("Salam Django")

def about_page(request):
    return HttpResponse("About Page")

def products__home__page(request):
    return HttpResponse("Products Home Page")


def products__list(request):
    return HttpResponse("Products List")

def products__about(request):
    return HttpResponse("Products About")