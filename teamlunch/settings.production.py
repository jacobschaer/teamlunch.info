from .settings_core import *
import os

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.expanduser('~/site-config/teamlunch.info/my.cnf'),
        },
    }
}


EMAIL_HOST = SITE_SETTINGS.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = SITE_SETTINGS.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = SITE_SETTINGS.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = SITE_SETTINGS.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = SITE_SETTINGS.get('EMAIL_USE_TLS', False)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
 )

STATIC_ROOT = os.path.join(BASE_DIR, "static")

ALLOWED_HOSTS = ['www.teamlunch.info', 'teamlunch.info']