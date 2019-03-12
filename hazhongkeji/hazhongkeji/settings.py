"""
Django settings for hazhongkeji project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bm3g3prtd&^6qo+=!wxat182arw0d7&!0v^=9p(5#4xw4q&+16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',    # allauth应用
    'allauth.account', # allauth应用
    'allauth.socialaccount', # allauth应用
    'allauth.socialaccount.providers.weixin', # allauth 微信应用
    'hazhongsite.apps.HazhongsiteConfig',
    'zhizhu_proxy.apps.ZhizhuConfig',
    'xiaohua_spider.apps.XiaohuaSpiderConfig',
    'hongchang.apps.HongchangConfig',
    'myauth.apps.MyauthConfig',
    'mdeditor',
    'rest_framework',
]
SITE_ID = 1    # allauth 配置

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hazhongkeji.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'hazhongkeji.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zhizhu',
        'USER': 'zhizhu',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'templates', 'static'),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

# STATICFILES_DIRS = (os.path.join('static'),)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static_collect'),
]


#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

MEDIA_URL = '/media/'

# DATABASE_ROUTERS = ['hazhongkeji.db_router.DatabaseAppsRouter',]
#
#
# DATABASE_APPS_MAPPING = {
#     'xiaohua_spider' : 'db1',
#
# }
#
