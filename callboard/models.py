from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class Category(models.Model):
    CATEGORY = [
        ('TN', 'Танки'),
        ('HL', 'Хилы'),
        ('DD', 'ДД'),
        ('MC', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QS', 'Квестгиверы'),
        ('BS', 'Кузнецы'),
        ('LW', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'),
    ]

    name = models.CharField(max_length=2, choices=CATEGORY)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Advert(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = MarkdownxField(blank=True)
    title = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Respond(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)


class News(models.Model):
    text = models.TextField()
