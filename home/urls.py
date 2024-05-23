from django.urls import path
from .views import products__list, products__home__page, products__about

urlpatterns = [
    path("", products__home__page), # http://127.0.0.1:8000/products/
    path("list", products__list), # http://127.0.0.1:8000/products/list
    path("about", products__about), # http://127.0.0.1:8000/products/about
]

# Salam
