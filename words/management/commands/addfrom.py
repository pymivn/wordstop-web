import os

from django.core.management.base import BaseCommand, CommandError
from words.models import Word, Book

import wordstop
from wordstop import gutenberg_stop_cond as _stop_cond


class Command(BaseCommand):
    help = 'Add words from given text file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        for f in options['file']:
            try:
                with open(f) as text:

                    bookinfo = wordstop.get_gutenberg_info(text)  # NOQA
                    if all(bookinfo.values()):
                        b = Book(**bookinfo)
                    else:
                        # Go back to the first line as this is not Gutenberg
                        # as we iterated to find out if the file is Gutenberg
                        name = os.path.basename(f)
                        b = Book(name=name)
                    b.save()

                    counts, examples = wordstop.count(text,
                                                      stop_cond=_stop_cond,
                                                      stop_word=False)
                    for word, count in counts.most_common(300):
                        w = Word(word=word,
                                 frequency=count,
                                 example=examples[word],
                                 book=b)
                        w.save()
            except OSError:
                raise CommandError('Cannot access %s file' % f)

            self.stdout.write(
                self.style.SUCCESS('Successfully import book "%s"' % f)
            )
