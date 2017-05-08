all: run

migrate:
	python manage.py makemigrations
	python manage.py makemigrations words
	python manage.py migrate

run: migrate
	python manage.py runserver

import:
	python manage.py addfrom pride_and_prejudice_sample.txt
	python manage.py addfrom django_sample.txt

init: migrate import


reset:
	rm -r db.sqlite3 words/migrations
