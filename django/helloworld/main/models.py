from django.db import models
from django.db.models import base
from django.db.models import fields


class Author(base.Model):
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=50)


class Book(base.Model):
    title = fields.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Publisher(base.Model):
    name = fields.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    books = models.ManyToManyField(Book)


# после каждого изменения модели
# py manage.py makemigrations main

# (опционально) компиляция SQL кода в файл
# py manage.py sqlmigrate %имя_приложения% %номер_миграции% > %имя_приложения%\migrations\%номер_миграции%.sql

# применить миграции
# py manage.py migrate
