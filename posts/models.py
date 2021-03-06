from django.conf import settings
#from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

import misaka

from communities.models import Community


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts")
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    community = models.ForeignKey(Community, related_name="posts", null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                # "pk": self.pk
               "slug": self.slug
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
