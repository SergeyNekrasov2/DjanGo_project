from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product

class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return ProductForm
    #     if user.has_perm('catalog.can_unpublish_product'):
    #         return ProductModeratorForm
    #     raise PermissionDenied
    # def get_success_url(self):
    #     return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    # def get_form_class(self):
    #     user = self.request.user
    #     if not user.has_perm('catalog.delete_product') or not user == self.object.owner:
    #         raise PermissionDenied
