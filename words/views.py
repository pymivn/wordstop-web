import logging
from django.views.generic import ListView, DetailView
from .models import Book, Word

logger = logging.getLogger(__name__)


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)

        context['words'] = Word.objects.filter(book_id=self.kwargs['id']).order_by('-frequency')  # NOQA
        return context
