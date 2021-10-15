from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=100, default='')
    source = models.CharField(default='', max_length=300)
    isbn = models.CharField(max_length=20, default='')
    language = models.CharField(max_length=20, default='English')

    class Meta:
        unique_together = ('name', 'author')

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=31)
    frequency = models.IntegerField(default=0)
    example = models.TextField(default='')
    translate_vi = models.TextField(default='')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
