from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Product
from .forms import ProductCreate

from cart.models import CartNew


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_obj = CartNew.objects.filter(user=self.request.user).first()
        product_added = cart_obj.product.all()
        context['product_added'] = product_added
        return context
