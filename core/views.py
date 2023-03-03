
from django.shortcuts import render
from django.views.generic import ListView
from core.models import Product
# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = "index.html"