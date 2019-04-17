"""dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dev.views import home
from contacts.views import contact
from . import views

urlpatterns = [
    url(r"^$", home, name="home"),
    url(r"^admin_musicalpacks_18nov1990/", include(admin.site.urls)),
    url(r"^contact/$", contact, name="contact"),
    # This uses the login views created in views.py
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    # This look through the registrations folder an log users
	# also @ settings.py we put LOGIN_REDIRECT_URL="page"
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^posts/", include("posts.urls", namespace="posts")),
    url(r"^articles/", include("articles.urls", namespace="articles")),
    url(r"^communities/", include("communities.urls", namespace="communities")),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),

    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^categories/', include('categories.urls', namespace='categories')),
]


urlpatterns += staticfiles_urlpatterns()
# Remove this conditional check if you want to upload to Heroku
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
