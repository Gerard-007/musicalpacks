from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.ArticleList.as_view(), name='article_list'),
	url(r'^(?P<slug>\d+)/$', views.ArticleDetail.as_view(), name='article_detail'),
	url(r'^create/$', views.ArticleCreate.as_view(), name='article_create'),
	url(r'^edit/(?P<slug>\d+)/$', views.ArticleUpdate.as_view(), name='article_update'),
	url(r'^delete/(?P<slug>\d+)/$', views.ArticleDelete.as_view(), name='article_delete'),
]
