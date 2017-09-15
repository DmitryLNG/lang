from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from shop.models import Category

class IndexView(ListView):
    model = Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'
