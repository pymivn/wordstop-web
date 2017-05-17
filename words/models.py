from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


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
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.word


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)

    def __str__(self):
        return str(self.user)


@receiver(models.signals.post_save, sender=User)
def create_new_worduser(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=user)
        profile.save()
