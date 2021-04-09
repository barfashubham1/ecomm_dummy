from django.shortcuts import render

from django.views import generic
from products.models import Cart


class HomePage(generic.TemplateView):
    model = Cart
    template_name = "index.html"
