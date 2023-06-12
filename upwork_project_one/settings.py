"""
Django settings for upwork_project_one project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
#from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop', # app Shop is added here
    'blog', # app Blog is added here
    'ckeditor', # add ckeditor
    'ckeditor_uploader', # add ckeditor_uploader   
    #'django.contrib.sites', # add sites
    'allauth', # add allauth
    'allauth.account', # add allauth.account
    'allauth.socialaccount', # add allauth.socialaccount
    'allauth.socialaccount.providers.google', # add allauth.socialaccount.providers.google
    'allauth.socialaccount.providers.facebook', # add allauth.socialaccount.providers.facebook
    'allauth.socialaccount.providers.instagram', # add allauth.socialaccount.providers.instagram

]
#SITE_ID = 1
SOCIALACCOUNT_LOGIN_ON_GET=True 
'''
    SOCIALACCOUNT_PROVIDERS IS USED TO os.environ.getURE SOCIAL ACCOUNTS
'''
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    
    },

}
LOGIN_REDIRECT_URL = '/' # REDIRECT TO HOME PAGE AFTER LOGIN
LOGOUT_REDIRECT_URL = '/' # REDIRECT TO HOME PAGE AFTER LOGOUT
#ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' # Could be useful if you are using SSL
ACCOUNT_AUTHENTICATION_METHOD = 'username_email' # ALLOW USERS TO LOGIN WITH EITHER USERNAME OR EMAIL (username for admins)

AUTHENTICATION_BACKENDS = [ # add AuthenticationBackend
    'django.contrib.auth.backends.ModelBackend', # add ModelBackend
    'allauth.account.auth_backends.AuthenticationBackend', # add allauth
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'upwork_project_one.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'upwork_project_one.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/' # static files will be served from this folder
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # path to static folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # path to media folder
MEDIA_URL = '/media/' # media files will be served from this folder

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_UPLOAD_PATH = "/media/" # path to media folder for ckeditor uploads
CKEDITOR_CONFIGS = { # add ckeditor config
    'default': { # default config
        'toolbar': 'Custom', # select toolbar
         'toolbar_Custom': [ # define toolbar
            ["Format", "Bold", "Italic", "Underline", "Strike",], # define buttons
            [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight'], # define buttons
            ["Image"], # define buttons 
            ['Undo', 'Redo']], # define buttons

    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # add email backend
EMAIL_HOST = os.environ.get('smtp_host') # add smtp host
EMAIL_PORT = 2525 # add smtp port
EMAIL_HOST_USER = os.environ.get('smtp_user') # add smtp user
EMAIL_HOST_PASSWORD = os.environ.get('smtp_password') # add smtp password
EMAIL_USE_TLS = True # add tls
EMAIL_USE_SSL = False # add ssl
DEFAULT_FROM_EMAIL = os.environ.get('default_from_mail')


CRONJOBS = [ # cron job to remove expired tokens
    ('0 * * * *', 'shop.cron.remove_tokens'),
]



