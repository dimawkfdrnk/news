from app_parser.models import News, Comments, Likes, ExchangeRates, AuthorsArticles
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import CommentForm, CreateAuthorsArticleForm


def main_page(request):
    rates = ExchangeRates.get_rates()
    articles = AuthorsArticles.get_authors_article()
    page_obj = News.objects.all()
    paginator = Paginator(page_obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        page_obj = News.objects.filter(title__search=request.POST.get('search'))

    context = {
        'page_obj': page_obj,
        'rates': rates,
        'articles': articles
    }

    return render(request, 'main_page/main_page.html', context)


def news_page(request, news_id):
    context_news = News.objects.get(id=news_id)
    like_user = Likes.objects.filter(user=request.user.id, news=news_id).count()
    liked = like_user == 0
    context = {
        'context_news': context_news,
        'comment_form': CommentForm(),
        'liked': liked,
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
    else:
        Comments.objects.filter(id=request.GET.get('comment_id')).delete()

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


def create_authors_articles(request):
    if request.method == "POST":
        form = CreateAuthorsArticleForm(request.POST)
        if form.is_valid():
            title = form['title'].value()
            text_article = form['text_article'].value()
            author = User.objects.get(username=request.user.username)
            AuthorsArticles.create_authors_article(title=title, author=author, text_article=text_article)

    lol = CreateAuthorsArticleForm()
    context = {
        'lol': lol
    }
    return render(request, 'main_page/authors_article.html', context)



