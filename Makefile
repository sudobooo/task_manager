install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

heroku_local:
	poetry export -f requirements.txt --output requirements.txt
	pip install -r requirements.txt
	poetry run python manage.py collectstatic
	heroku local

runserver:
	poetry run python manage.py runserver 127.0.0.1:8000
