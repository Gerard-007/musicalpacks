from django import forms
from django.forms import ModelForm
from pagedown.widgets import PagedownWidget
from articles.models import Article, Comment, Category

class ArticleForm(forms.ModelForm):
    published = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Article
        fields = ("category",
                    "title",
                    "image",
                    "body",
                    "draft",)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
