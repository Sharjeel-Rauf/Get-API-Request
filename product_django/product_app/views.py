from django.shortcuts import render
from django.views import View
from .models import Product


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'product_app/product_list.html', {'products': products})