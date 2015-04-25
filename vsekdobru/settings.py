# -*- coding: utf-8 -*-
"""
Django settings for vsekdobru project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '729a583k%9@5r%s22p)+knl$-s@rx3)roxm$jfsb)#-n)$et1e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#   Данные для admin_tools
ADMIN_TOOLS_INDEX_DASHBOARD = 'vsekdobru.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'vsekdobru.dashboard.CustomAppIndexDashboard'
# Application definition

PROJECT_APPS = (  # Мои модули
                  'invitations',
                  'accounts',
                  'ideas',
                  'facts',
                  )

BATTERY_APPS = (  # Приложения пакета allauth
                  'allauth',
                  'allauth.account',
                  'allauth.socialaccount',
                  # ... include the providers you want to enable:
                  'allauth.socialaccount.providers.facebook',
                  'allauth.socialaccount.providers.google',
                  'allauth.socialaccount.providers.instagram',
                  'allauth.socialaccount.providers.linkedin',
                  'allauth.socialaccount.providers.linkedin_oauth2',
                  'allauth.socialaccount.providers.odnoklassniki',
                  'allauth.socialaccount.providers.twitter',
                  'allauth.socialaccount.providers.vk',
                  # 'django_extensions',
                  'pagination',
                  'sorl.thumbnail',
                  'django_resized',
                  )
INSTALLED_APPS = (
    # Приложения  пакета admin_tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    # Стандартные приложения
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
                 ) + PROJECT_APPS + BATTERY_APPS

SITE_ID = 1         # Для allauth модуля

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'vsekdobru.urls'

# CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:8000',
#    }
#}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/templates/',
            '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/ideas/templates/',
            '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/accounts/templates/',
            '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/facts/templates/',
            '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/invitations/templates/',

                 ],
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

TEMPLATE_CONTEXT_PROCESSORS = (
# Required by `allauth` template tags
"django.core.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
'django.core.context_processors.request',
"django.contrib.auth.context_processors.auth",
#`allauth` specific context processors
'allauth.account.context_processors.account',
'allauth.socialaccount.context_processors.socialaccount',
)

WSGI_APPLICATION = 'vsekdobru.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static', 'fotos'),
    # "static", '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/static',
    # '/Users/dobrodel/Developer/envDjangoSite/bin/vsekdobru/static/fotos',
)
MEDIA_URL = '/static/fotos/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'fotos')
THUMBNAIL_DEBUG = True
# ------------------------------------------------------------------------------------------
#  Изменения касаемые расширения стандатной аутификации
# ------------------------------------------------------------------------------------------
AUTH_PROFILE_MODULE = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ('accounts.backends.CustomUserModelBackend',
                           #'allauth' specific authentication methods, such as login by e-mail
                           'allauth.account.auth_backends.AuthenticationBackend',
                           )
# invitations
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_BLACKLIST = ['dobrodel','idobrodel', 'admin', 'root', 'adam']
#
#   Переопределяю форму Регистрации модуля allauth
#
# Add to settings.py, django-allauth setting
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'
#ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SignupForm'
INVITATIONS_INVITATION_ONLY = True
INVITATIONS_SIGNUP_REDIRECT = '/accounts/signup/'

LOGIN_REDIRECT_URL = ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/facts/'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = \
    { 'facebook':
          { 'SCOPE': ['email', 'public_profile', 'user_friends'],
            'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
            'METHOD': 'oauth2',
            'LOCALE_FUNC': lambda request: 'ru_RU',
            'VERIFIED_EMAIL': False,
            'VERSION': 'v2.3' } }


#-----------------------------------------------------
#
#   Настройка почтового сервера
#
# -----------------------------------------------------
#EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'admin@dobtowest.ruuuuu'
#EMAIL_HOST_PASSWORD = 'pw'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True


'''
    selenium - тестовый сервер приложений
'''

