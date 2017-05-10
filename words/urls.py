from django.conf.urls import url

from . import views
app_name = 'books'

urlpatterns = [
    # ex: /books/
    url(r'^$', views.BookList.as_view()),
    # ex: /books/5/
    url(r'^(?P<id>[0-9]+)/$', views.BookDetail.as_view()),
]
