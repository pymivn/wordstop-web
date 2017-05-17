from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Book, Word, Profile


class BookList(ListView):
    model = Book


# TODO(HVN) add words by choice item and submit form
class BookDetail(DetailView):
    model = Book
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)

        context['words'] = Word.objects.filter(book_id=self.kwargs['id']).order_by('-frequency')  # NOQA
        return context


# TODO(HVN) handle when logged in user access /login
# TODO(HVN) hide words, mark as learnt
@login_required
def profile(request):
    p = Profile.objects.get(user_id=request.user.id)
    context = {'words': p.words.all()}

    return render(request, 'words/profile.html', context)
