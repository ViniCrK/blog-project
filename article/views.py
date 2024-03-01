from django.shortcuts import render

articles = [
    {
        'title': ...,
        'subtitle': ...,
        'content': ...,
    }
]


def list_articles(request):
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)
