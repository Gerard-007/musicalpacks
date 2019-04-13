"""
Django settings for dev project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sendgrid
import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hwz12fud7',
    'API_KEY': '314466862822259',
    'API_SECRET': 'fzM2SW-kUAm8dcA3gvLIhO5IGu4'
}

SEND_GRID_API_KEY = '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'
EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST = 'mail.musicadence.com'
EMAIL_HOST_USER = 'geetechcypher@gmail.com'
EMAIL_HOST_PASSWORD = '18nov1990'
EMAIL_PORT = '25'
EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_PORT = '465'
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = 'info@musicadence.com'
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
# ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email recieved from musicadence.com'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k@!2j4=)qvxlb7f@k^scnp#_sxe6enu30@$#(@694w5t993ps#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    # Third Party apps
    'cloudinary_storage',
    'cloudinary',
    'storages',
    'widget_tweaks',
    'pagedown',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'bootstrap3',

    # My Apps
    'accounts',
    'articles',
    'contacts',
    'communities',
    'posts',
    'books',
    'categories',
]

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'dev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#Login redirect url
LOGIN_REDIRECT_URL = 'home'

# cloudinary media setups for images and videos
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_ROOT = MEDIA_URL

#ckeditor upload path...
CKEDITOR_UPLOAD_PATH = DEFAULT_FILE_STORAGE

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        # 'height': 300,
        # 'width': 300,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['RemoveFormat', 'SpecialChar', 'CodeSnippet', 'Source' ],
        ],
        'extraPlugins': 'codesnippet',
    },
    'userEdit': {
        'toolbar': 'UserEdit',
        'toolbar_UserEdit': [
            ['Bold', 'Italic', 'Underline', 'CodeSnippet'],
            ['Link', 'Unlink'],
        ],
        'extraPlugins': 'codesnippet',
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
