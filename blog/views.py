from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.http import require_GET

from .models import Post


@require_GET
def blog_list(request: HttpRequest):
    return render(request, 'blog/post_list.html')


def post_detail(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Post, slug=post_slug)
    return HttpResponse(f'<br><br><b>{post.title}</b>')


def error404(request, exception):
    return render(request, 'blog/error404.html')
