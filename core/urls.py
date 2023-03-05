from django.urls import path
from core.views import *


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("index.html", IndexView.as_view(), name="home"),
    path('product/<slug>/', ProductDetailView.as_view(), name='product-detail'),
]
