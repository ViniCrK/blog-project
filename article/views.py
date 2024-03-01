from django.shortcuts import render

articles = [
    {
        'id': 1,
        'title': "Verstappen's on pole for F1 season-opening Bahrain Grand Prix, as drama over his boss intensifies",
        'subtitle': ...,
        'content': ...,
    }
]


def list_articles(request):
    return render(request, 'index.html')


def detail_article(request):
    context = {
        'articles': articles,
    }
    return render(request, 'detail_article.html', context)
