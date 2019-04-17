import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )

from books.forms import BookForm
from books.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from books.models import Book


class BookCreateView(StaffMemberRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    #success_url = "/success/"


class BookDetailView(MemberRequiredMixin, DetailView):
    queryset = Book.objects.all()


class BookListView(ListView):
    def get_queryset(self):
        request = self.request
        qs = Book.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs


class BookUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Book.objects.all()
    form_class = BookForm


class BookDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Book.objects.all()
    #success_url = '/books/'
