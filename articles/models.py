# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
#from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


def upload_dir(instance, filename):
    return "{}/{}".format(instance.author, filename)

class ArticleQuerySet(models.query.QuerySet):
    def not_draft(self):
        return self.filter(draft=False)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().not_draft()


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL)

	class Meta:
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("articles_by_category", args=[self.name])


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to=upload_dir, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    published = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category)
    objects = ArticleManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_img_url(self, default_path="../img/icons/musicadence.jpg"):
        if self.image:
            return self.image
        return default_path

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
            return "Photo <{}:{}>".format(self.title, public_id)

    def get_absolute_url(self):
        return reverse("articles:article_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('-published',)
        unique_together = ["slug", "title",]
        db_table = "article"


def article_pre_save_signal(sender, instance, *args, **kwargs):
    # instance = "Second Post" -- post title
    if not instance.slug:
        instance.slug = slugify(instance.title)
        new_slug = "{}-{}" .format(instance.title, instance.id)
        try:
            slug_exists = Article.objects.get(slug=instance.slug)
            instance.slug = slugify(new_slug)
        except Post.DoesNotExist:
            instance.slug = instance.slug
        except Post.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
        except:
            pass

pre_save.connect(article_pre_save_signal, sender=Article)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #settings.AUTH_USER_MODEL, default=1
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
    	self.approved = True
    	self.save()

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['created']
