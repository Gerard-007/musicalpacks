from django.shortcuts import render
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView,
        RedirectView
    )

from categories.models import Category


class CategoryListView(ListView):
    queryset = Category.objects.all().order_by('title')


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = context.get("object")
        user = self.request.user
        return context
