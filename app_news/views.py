from app_parser.models import News, Comments, Likes
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CommentForm


def main_page(request):
    if request.method == "POST":
        page_obj = News.objects.filter(title__search=request.POST.get('search'))
    else:
        page_obj = News.objects.all()
        paginator = Paginator(page_obj, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
    }
    return render(request, 'main_page/main_page.html', context)


def news_page(request, news_id):
    context_news = News.objects.get(id=news_id)
    comments = Comments.objects.filter(news=news_id)
    a = Likes.objects.filter(user=request.user.id, news=news_id).count()
    ind = a == 0
    context = {
        'context_news': context_news,
        'comments': comments,
        'comment_form': CommentForm(),
        "ind": ind
    }
    return render(request, 'main_page/news_page.html', context)


def comments(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comments.objects.create(
                **form.cleaned_data,
                news_id=request.POST.get('news_id'),
                user=User.objects.get(username=request.user.username)
            )

    return redirect(request.META['HTTP_REFERER'])


def likes(request):
    if request.method == "POST":
        Likes.objects.create(
            news_id=request.POST.get('news_id'), user=User.objects.get(username=request.user.username))
    return redirect(request.META['HTTP_REFERER'])


def delete_like(request):
    if request.method == "POST":
        Likes.objects.filter(
            user=request.user.id, news=request.POST.get('news_id')).delete()
    return redirect(request.META['HTTP_REFERER'])
