from django import forms


from books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'cover_picture',
            'price',
            'contributors'
        ]
