from django.shortcuts import render
from .models import Article


def list_articles(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'article/index.html', context)


def detail_article(request, id):
    article = Article.objects.prefetch_related('tags').get(pk=id)

    context = {
        'article': article,
    }
    return render(request, 'article/detail_article.html', context)
