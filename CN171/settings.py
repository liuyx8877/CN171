"""
Django settings for CN171 project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import pymysql
import os
try:
    import ConfigParser as cp
except ImportError as e:
    import configparser as cp

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = cp.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config/cn171.conf'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '42427w*ffn#8a&!@8bd*ia^j93&0$ufe#re*5dmt&&l^y-0jj5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CN171_account',
    'CN171_background',
    'CN171_cmdb',
    'CN171_config',
    'CN171_login',
    'CN171_monitor',
    'CN171_order',
    'CN171_crontab',
    'djcelery',

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

ROOT_URLCONF = 'CN171.urls'

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

WSGI_APPLICATION = 'CN171.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

pymysql.install_as_MySQLdb()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.get('DataBase', 'database'),
        'USER': config.get('DataBase', 'user'),
        'PASSWORD': config.get('DataBase', 'password'),
        'HOST': config.get('DataBase', 'host'),
        'PORT': config.getint('DataBase', 'port'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# 设置邮件域名
EMAIL_HOST = 'smtp.163.com'
# 设置端口号，为数字
EMAIL_PORT = 25
#设置发件人邮箱
EMAIL_HOST_USER = config.get('PBOSS', 'pboss_order_mail_inbox')
# 设置发件人 授权码
EMAIL_HOST_PASSWORD = config.get('PBOSS', 'pboss_order_mail_password')
# 设置是否启用安全链接
EMAIL_USER_TLS = True




#Celery配置
# import djcelery
# djcelery.setup_loader()
# BROKER_BACKEND = 'redis'
# BROKER_URL = 'redis://39.104.61.178:6379/1'
# CELERY_RESULT_BACKEND = 'redis://39.104.61.178:6379/2'  #不配置则直接使用默认数据库
# CELERY_IMPORTS = ('CN171_crontab.tasks', )
# CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'



# Broker配置，使用Redis作为消息中间件
BROKER_URL = 'redis://39.104.61.178:6379/1'

# BACKEND配置，使用django orm作为结果存储
CELERY_RESULT_BACKEND = 'redis://39.104.61.178:6379/2'

# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json'

#设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'

#设置beat数据库
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


