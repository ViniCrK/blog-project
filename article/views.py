from django.shortcuts import render

articles = [
    {
        'id': 1,
        'title': "Max Verstappen wins Bahrain Grand Prix amid Red Bull turmoil",
        'subtitle': "It was a commanding one-two win for Red Bull with teammate Sergio Perez",
        'content': "SAKHIR, Bahrain — The ongoing drama around Red Bull had no effect on its three-time reigning world champion as Max Verstappen routed the field by 22 seconds in the season-opening Formula 1 race on Saturday.\n Verstappen started the Bahrain Grand Prix on pole position and was never seriously challenged on his way to a commanding one-two win for Red Bull with teammate Sergio Perez. Embattled team principal Christian Horner was joined before the race and during the podium celebration by his former pop star wife, Geri Halliwell.",
    },
    {
        'id': 2,
        'title': "The politics and economics behind Biden's China-car espionage probe",
        'subtitle': "The administration is throwing out some scary scenarios",
        'content': "WASHINGTON — President Joe Biden, vowing to 'do right by U.S. autoworkers', launched an investigation this week into whether Chinese-made vehicles could be used to spy on Americans, a far-off threat given the few such cars on U.S. roads now. The White House announced the probe Thursday citing national-security risks about 'connected' cars creating 'new avenues for espionage and sabotage.'",
    },
]


def list_articles(request):
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def detail_article(request, id):
    context = {
        'article': articles[id - 1],
    }
    return render(request, 'detail_article.html', context)
