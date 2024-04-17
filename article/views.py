from django.shortcuts import render
from .models import Article


def list_articles(request):
    context = {
        'articles': Article.objects.all()
    }

    return render(request, 'article/index.html', context)


def detail_article(request, id):
    article = Article.objects.prefetch_related('tags').get(pk=id)

    context = {
        'article': article,
    }
    return render(request, 'article/detail_article.html', context)
