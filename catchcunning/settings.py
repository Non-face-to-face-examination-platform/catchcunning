from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*', 'catchcunning.site', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'meeting',

    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'sslserver',  # nginx에서 letsencrypt로 인증서 자동 발급해서 사용 x
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

ROOT_URLCONF = 'catchcunning.urls'

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

WSGI_APPLICATION = 'catchcunning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('DBNAME'),
        'Host': env('DBHOST'),
        'PORT': env('DBPORT'),
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPW'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "user.validators.CustomPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = env('STATIC_URL')
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = "user.User"


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SINGUP_REDIRECT_URL = "lobby"
LOGIN_REDIRECT_URL = "lobby"

ACCOUNT_LOGOUT_ON_GET = "True"
ACCOUNT_AUTHENTICATION_METHOD = "email"  # username_email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False  # 유저네임 필드 삭제
ACCOUNT_SIGNUP_FORM_CLASS = "user.forms.SignupForm"
ACCOUNT_SESSION_REMEMBER = False  # 항상 기억할지(브라우저 종료해도)
# SEESION_COOKIE_AGE = 3600           #쿠기 유지 시간(초단위, 기본시간 2주?)
# 만료된 세션 아이디는 자동으로 삭제 안 됨 -> python manage.py clearsessions
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False  # 비번은 유지
ACCOUNT_EMAIL_VARIFICATION = "none"
# mandatory 무조건 인증, optional 인증 안해도 디폴트 값, none 아예 인증 필요x
ACCOUNT_CONFIEM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = {
    "account_email_confirmation_done"
}  # 로그인 됐을 때
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_cofirmation_done"  # 로그인 안 됐을 때
PASSWORD_RESET_TIMEOUT_DAYS = 3600
# 장고 3.0 버전 이전은 TIMEOUT_DAYS = 단위 일, 3.1 이후는 TIMOUT = 단위 초
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""


# Email Settings

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# 미디어

MEDIA_URL = env('MEDIA_URL')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
