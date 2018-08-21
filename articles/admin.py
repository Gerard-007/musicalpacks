# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Article, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'published')
	list_filter = ('author', 'created', 'published')
	search_field = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'body', 'approved')

admin.site.register(Comment, CommentAdmin)
