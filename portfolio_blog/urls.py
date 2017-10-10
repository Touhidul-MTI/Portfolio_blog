from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from portfolio_blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20],
                                template_name="portfolio_blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                             template_name='portfolio_blog/post.html')),
    ]
