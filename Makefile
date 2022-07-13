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

run:
	poetry run python manage.py runserver
