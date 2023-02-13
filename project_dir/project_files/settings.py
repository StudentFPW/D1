import os
from pathlib import Path

########################################################################################################################

# Это способ получить каталог текущего файла.
BASE_DIR = Path(__file__).resolve().parent.parent

########################################################################################################################

SECRET_KEY = 'django-insecure-h=^p@u+fa7mtho8&oqwag7=n962%-mdg&ucd(_))qd*yte*&ro'

DEBUG = True

ALLOWED_HOSTS = []

########################################################################################################################

# Это список всех приложений, установленных в проекте.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Приложение позволяет создавать и редактировать страницы сайта в админке ↓
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Пользовательское приложение, которое используется для прав доступа и комментирования ↓
    'fpages',
]

# ----------------------------------------------------------------------------------------------------------------------

# Настройка для фреймворка django.contrib.sites
SITE_ID = 1

# ----------------------------------------------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Приложение позволяет создавать и редактировать страницы сайта в админке.
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

# ----------------------------------------------------------------------------------------------------------------------

ROOT_URLCONF = 'project_files.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Указание Django искать шаблоны в каталоге шаблонов.
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

########################################################################################################################

WSGI_APPLICATION = 'project_files.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

########################################################################################################################

# Он говорит Django искать статические файлы в статическом каталоге проекта.
STATICFILES_DIRS = [BASE_DIR / "static"]

########################################################################################################################
