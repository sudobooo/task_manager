### Hexlet tests and linter status:
[![Actions Status](https://github.com/sudobooo/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/sudobooo/python-project-lvl4/actions)
[![Python CI](https://github.com/sudobooo/python-project-lvl4/actions/workflows/pyci.yml/badge.svg)](https://github.com/sudobooo/python-project-lvl4/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e4b98cb6d78c3f19e4a4/maintainability)](https://codeclimate.com/github/sudobooo/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e4b98cb6d78c3f19e4a4/test_coverage)](https://codeclimate.com/github/sudobooo/python-project-lvl4/test_coverage)


# Task Manager

The fourth project written for the academic purposes of a Hexlet's course on learning a programming language Python.

View the work of the Task Manager on [Heroku](https://vibrant-madame-12861.herokuapp.com/)

## About the project

Task Manager is an Internet application that can be used by several users at the same time. Implemented registration and authorization. Tasks have labels and statuses.

## How to install and use

### Install
```
git clone https://github.com/sudobooo/python-project-lvl4
cd python-project-lvl4
make install
```

### Environment variables

For the application to work, you need to create a file .env in the root of the project.

Then open the file and set any value for the SECRET_KEY=<anything>

If you want to enable debug mode, then set for the DEBUG=Yes

### Running the application on a local server

```
make runserver
```

### Database

If you want to use the PostgreSQL, then set for environment variable the DB_POSTGRES=True
Then the required values for the following variables:
POSTGRES_NAME=<database_name>
POSTGRES_USER=<database_user>
POSTGRES_PASSWORD=<user_password>
POSTGRES_HOST=<database_host>
POSTGRES_PORT=<database_port>

### Run migrations

```
make migrate
```

### Logging

Rollbar is used for logging.

Set for environment variable the ACCESS_TOKEN=<token_of_your_account_in_rollbar>

### Language

If you want to change the language to English, then in task_manager/settings change the value of LANGUAGE_CODE to "en"

If you want to add another language, then use the following [guide](https://djangowaves.com/tutorial/multiple-languages-in-Django).
Start right away with the chapter "Create translations with Django"
