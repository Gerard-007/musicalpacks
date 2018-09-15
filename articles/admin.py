# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from .models import Article, Comment, Category
# from pagedown.widgets import AdminPagedownWidget
# Register your models here.

admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'published', 'category')
	list_filter = ('author', 'created', 'published', 'category')
	search_field = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	# formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget },
    # }

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'body', 'approved')

admin.site.register(Comment, CommentAdmin)
