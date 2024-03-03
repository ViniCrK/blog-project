from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:id>/', views.detail_article, name='detail_article'),
    path('', views.list_articles, name='list_articles'),
]
