from __future__ import unicode_literals
from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
   prepopulated_fields = {"slug": ("message",)}

admin.site.register(models.Post, PostAdmin)


# admin.site.register(models.Post)
