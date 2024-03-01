from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.detail_article, name='detail_article'),
    path('', views.list_articles),
]
