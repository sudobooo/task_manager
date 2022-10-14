install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

push-heroku:
	poetry export -f requirements.txt --output requirements.txt
	poetry run python manage.py collectstatic
	heroku run python manage.py makemigrations -a vibrant-madame-12861
	heroku run python manage.py migrate -a vibrant-madame-12861

runserver:
	poetry run python manage.py runserver 127.0.0.1:8000

prepare-translation:
	django-admin makemessages --ignore="static" --ignore=".env"  -l en

complete-translation:
	poetry run django-admin compilemessages

createsuperuser:
	poetry run python manage.py createsuperuser
