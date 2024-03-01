from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:id>/', views.detail_article),
    path('list_articles/', views.list_articles),
]
