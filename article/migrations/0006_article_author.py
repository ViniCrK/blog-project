# Generated by Django 5.0.4 on 2024-04-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]