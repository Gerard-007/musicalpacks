from django.conf.urls import url, include
from django.views.generic import FormView
from articles import views
# from .forms import ArticleForm

urlpatterns = [
	url(r'^delete/(?P<slug>[\w-]+)/$', views.ArticleDelete.as_view(), name='article_delete'),
	url(r'^update/(?P<slug>[\w-]+)/$', views.ArticleUpdate.as_view(), name='article_update'),
	url(r'^dashboard/$', views.DashBoard.as_view(), name='article_dashboard'),
	url(r'^create/$', views.ArticleCreate.as_view(), name='article_create'),
	url(r'^details/(?P<slug>[\w-]+)$', views.ArticleDetail.as_view(), name='article_detail'),
	url(r'^$', views.ArticleList.as_view(), name='article_list'),
]
