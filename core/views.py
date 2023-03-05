
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import *
# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products_list"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product-detail.html"
