from django.db import models
from .category import Category
from .tag import Tag


class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f'{self.title}'
