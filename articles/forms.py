from django import forms
from django.forms import ModelForm
from articles.models import Article, Comment, Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("category",
                    "title",
                    "description",
                    "image",
                    "body",
                    "draft",)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'btn btn-raised btn-round btn-default btn-file'}),
        }

# class CommentForm(forms.Form):
#     content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ('content',)
