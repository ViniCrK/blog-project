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
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def detail_article(request):
    return render(request, 'detail.html')
