from django.contrib.auth.models import User
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, ArticleCreatorForm
from blog.schemas import ARTICLE_SCHEMA
from index_page.models import Portfolios, Project
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from jsonschema import ValidationError, validate


class CreateArticle(View):
    def get(self, request, user_id):
        if request.user.is_authenticated and request.user.id == int(user_id):
            context = {
                "form": ArticleCreatorForm(request.user.pk),
                "user_id": request.user.id
            }
            return render(request, "article_creator.html", context=context)
        else:
            if not request.user.is_authenticated:
                return redirect("login")
            else:
                return redirect("article_creation", request.user.id)

    def post(self, request, user_id):
        if request.user.is_authenticated and request.user.id == int(user_id):
            try:
                user_name = User.objects.get(id=user_id)
                validate(dict(request.POST), ARTICLE_SCHEMA)
                body_article = request.POST['body']
                image_article = request.FILES.get('image', None)
                title_article = request.POST['title']
                header_article = request.POST['header']

                # print(dict(request.POST)['categories'])  # (!!!! request.POST['categories'] --> 1 element)
                if dict(request.POST).get('categories') is not None:
                    categories = dict(request.POST).get('categories')
                else:
                    categories = []

                all_categories = list(Category.objects.filter(id__in=categories))

                if request.POST['new_category'] != '':
                    extended_category = Project(
                        user_portfolio=Portfolios.objects.get(id=request.POST.get('field_knowledge', 2)),
                        title=request.POST['new_category'],
                        description='TEST',
                    )

                    extended_category.save()

                    category = Category(
                        name=request.POST['new_category'],
                        user=request.user,
                        project=extended_category
                    )  # add function to add multiple categories via splitter
                    category.save()

                    all_categories.append(category)

                article = Post(
                    user=user_name, title=title_article, body=body_article, image=image_article, header=header_article,
                )
                article.save()

                for category in all_categories:
                    article.categories.add(category)

                return redirect("article_index", user_id)
            except ValidationError as exc:
                return JsonResponse({'error': exc.message}, status=401)
        else:
            if not request.user.is_authenticated:
                return redirect("login")
            else:
                return redirect("article_creation", request.user.id)


def article_dlt(request, user_id, pk):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(id=request.user.pk)
            posts = Post.objects.filter(user=user)
            post = posts.get(id=pk)
            post.delete()

            return redirect("article_index", request.user.pk)
        except:
            return HttpResponse(status=401)
    else:
        return redirect("login")


def article_index(request, user):
    try:
        user = User.objects.get(id=user)
        posts = Post.objects.filter(user=user).order_by('-created_on')
        # print(posts)
        context = {
            "posts": posts,
            "user_id": user.id,
            "is_user": request.user.is_authenticated
        }
    except:
        return HttpResponse(status=401)

    if request.user.is_authenticated:
        context.update({"user": True})
        return render(request, "article_index.html", context)
    else:
        context.update({"user": False})
        return render(request, "article_index.html", context)


def article_category(request, user_id, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts,
        "current_user_id": request.user.pk,  # For delete article
        "user_id": user_id
    }
    return render(request, "article_category.html", context)


def article_detail(request, user_id, pk):
    try:
        user = User.objects.get(id=user_id)
        post = Post.objects.get(pk=pk, user=user)  # for exist post could be his user (/blog/@1/12)
        comments = Comment.objects.filter(post=post)
        context = {
            "comments": comments,
            "post": post,
            "user": user_id
        }

        if request.user.is_authenticated:
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

            context.update({"form": form})
    except:
        return HttpResponse(status=401)

    return render(request, "article_detail.html", context)

