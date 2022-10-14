from pathlib import Path
from dotenv import load_dotenv
import os
import django_heroku
import rollbar


load_dotenv()
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv('DEBUG', 'true').lower() in ['true']

ALLOWED_HOSTS = [
    'vibrant-madame-12861.herokuapp.com',
    'localhost',
    '0.0.0.0',
    'webserver',
    '127.0.0.1',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task_manager',
    'task_manager.users',
    'task_manager.statuses',
    'task_manager.tasks',
    'task_manager.labels',
    'bootstrap4',
    'rest_framework',
    'task_manager.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'task_manager/templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_manager.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


POSTGRES_DATABASES = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('POSTGRES_NAME'),
    'USER': os.getenv('POSTGRES_USER'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'HOST': os.getenv('POSTGRES_HOST'),
    'PORT': os.getenv('POSTGRES_PORT'),
}

if os.getenv('DB_POSTGRES') in ['True']:
    DATABASES['default'] = POSTGRES_DATABASES

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa E501
    },
]


LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("ru", "Russian"),
    ("en", "English"),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'task_manager/locale'),)


STATIC_ROOT = os.path.join(BASE_DIR, 'task_manager/staticfiles')
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'task_manager/static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

django_heroku.settings(locals(), staticfiles=False, databases=False)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.ApplicationUsers'

ROLLBAR = {
    'access_token': os.getenv('ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}

rollbar.init(**ROLLBAR)
