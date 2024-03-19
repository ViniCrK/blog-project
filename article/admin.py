from django.contrib import admin
from .models.tag import Tag
from .models.category import Category
from .models.article import Article


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
