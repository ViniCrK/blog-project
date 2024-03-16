from django.contrib import admin
from article import models


@admin.register(models.Category)
class CateogryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = '-id',
    search_fields = 'title', 'subtitle',
    list_per_page = 10
    list_display_links = 'id', 'title',
