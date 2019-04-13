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
        print(obj)
        # user = self.request.user
        # qs1 = obj.book_set #.owned(self.request.user)
        # print(qs1)
        # context['featured_courses'] = qs1[:6]
        # qs2 = obj.secondary_category.all().owned(self.request.user)
        # qs = (qs1 | qs2).distinct()
        # context['courses'] = qs
        return context
