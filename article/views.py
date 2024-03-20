from django.shortcuts import render
from .models import Article


def list_articles(request):
    context = {
        'articles': Article.objects.all()
    }

    return render(request, 'index.html', context)


def detail_article(request, id):
    context = {
        'article': Article.objects.get(pk=id),
    }
    return render(request, 'detail_article.html', context)
