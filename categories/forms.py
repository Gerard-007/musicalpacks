from django import forms
from django.db.models import Q

from books.models import Book
from categories.models import Category



class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'book',
            'description',
            'slug',
        ]
    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get("instance")
        qs = Book.objects.all().unused()
        if obj:
            if obj.book:
                this_ = Book.objects.filter(pk=obj.book.pk)
                qs = (qs | this_)
            self.fields['book'].queryset = qs
        else:
            self.fields['book'].queryset = qs
