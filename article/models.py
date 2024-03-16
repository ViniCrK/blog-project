from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
