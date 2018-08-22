# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
# from django.views.generic import CreateView, ListView

#from . import mixins
from .models import Article, Comment



class ArticleList(generic.CreateView, generic.ListView):
	fields = ("author", "title", "body", "published")
	model = Article
	context_object_name = 'articles'
	paginate_by = 6
	template_name = "articles/article_list.html"

class ArticleDetail(generic.DetailView, generic.UpdateView):
	fields = ("author", "title", "body", "published")
	model = Article
	context_object_name = 'article'
	template_name = 'articles/article_detail.html'

class ArticleCreate(LoginRequiredMixin, generic.CreateView):
	fields = ("author", "title", "body", "published")
	model = Article

class ArticleUpdate(LoginRequiredMixin, generic.UpdateView):
	fields = ("author", "title", "body", "published")
	model = Article
	# Here we print out the name of the page updated
	def get_page_title(self):
		obj = self.get_object()
		return "Update {}".format(obj.name)

class ArticleDelete(LoginRequiredMixin, generic.DeleteView):
	model = Article
	success_url = reverse_lazy("articles:list")
	# Here we overide the delete function to only work if a user is a superuser
	def get_queryset(self):
		if not self.request.user.is_superuser:
			return self.model.objects.filter(author=self.request.user)
		return self.model.objects.all()

class CreateArticleComment(generic.CreateView):
	model = Comment
	fields = ('body',)
	context_object_name = 'comments'

	def post_valid(self, form):
		article = get_object_or_404(Article, slug=article.slug)
		articlecomment = form.save(commit=False)
		articlecomment.user = self.request.user
		articlecomment.article = article
		articlecomment.save()
		return redirect('articles:article_detail', slug=article.slug)

	def get_success_url(self):
		return reverse_lazy('articles:article_list')
