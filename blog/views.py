from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from .models import Post


def blog_list(request: HttpRequest):
    return HttpResponse('<br><br><b>Hello</b>')


def post_detail(request: HttpRequest, post_slug: str):
    post = Post.objects.get(slug=post_slug)
    return HttpResponse(f'<br><br><b>{post.title}</b>')
