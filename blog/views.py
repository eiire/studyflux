from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from blog.models import Post, Comment
from .forms import CommentForm


class CreateArticle(View):
    def get(sel, request, user):
        if request.user.is_authenticated and request.user.id == int(user):
            return render(request, "article.html")
        else:
            return HttpResponse(status=404)


def blog_index(request, user):
    try:
        user = User.objects.get(id=user)
        posts = Post.objects.filter(user=user).order_by('-created_on')
        context = {"posts": posts}
    except:
        return HttpResponse(status=404, content_type='User does not exist')

    if request.user.is_authenticated:
        context.update({"user": True})
        return render(request, "article_index.html", context)
    else:
        context.update({"user": False})
        return render(request, "article_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "article_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "article_detail.html", context)
