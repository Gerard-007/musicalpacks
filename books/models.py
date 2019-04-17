from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

from books.utils import create_slug

# Create your models here.

def upload_dir(instance, filename):
    return "{}/{}".format(instance.author, filename)

class Contributor(models.Model):
    # TODO: Define fields here
    handle = models.CharField(max_length=100, blank=True, null=True, unique=True)
    contributors = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'contributor'
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'

    def __str__(self):
        return self.handle


class BookQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(disabled=False)

    def unused(self):
        return self.filter(Q(category__isnull=True))


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()


class Book(models.Model):
    # TODO: Define fields here
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, blank=True)
    title = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    cover_picture = models.ImageField(upload_to=upload_dir, height_field=50, width_field=30, blank=True, null=True)
    disabled = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)
    price = models.CharField(default='500.00', blank=True, max_length=100)
    free = models.BooleanField(default=True)
    member_required = models.BooleanField(default=False)
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    updated = models.DateTimeField(auto_now=True)

    objects = BookManager()

    class Meta:
        ordering = ('title',)
        unique_together = ["slug", "title",]
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'https://res.cloudinary.com/hwz12fud7/image/upload/v1538131159/media/musicadence/musicadence.jpg'

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"slug": self.slug})

def pre_save_book_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_book_receiver, sender=Book)
