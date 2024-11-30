import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key-here')  # Keep this secret in production!

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'a9206bda41e140089021150bcf2d5927.vfs.cloud9.us-east-1.amazonaws.com',  # For development on Cloud9
    '.yourdomain.com',  # Replace with your domain in production
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'airline',  # Your app
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

ROOT_URLCONF = 'airline_project.urls'

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://a9206bda41e140089021150bcf2d5927.vfs.cloud9.us-east-1.amazonaws.com',
    'https://*.yourdomain.com',  # Replace with your domain in production
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'airline/templates'],  # Explicit template folder path
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

WSGI_APPLICATION = 'airline_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite for development
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directory for static files during development
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Collected static files for production

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login and Logout
LOGIN_REDIRECT_URL = 'home'  # Redirect after login
LOGOUT_REDIRECT_URL = 'home'  # Redirect after logout

# Debugging Email Backend (Change this in production)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Production Security Settings (Adjust as needed)
if not DEBUG:
    SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
    CSRF_COOKIE_SECURE = True  # Ensure CSRF cookie is sent over HTTPS
    SESSION_COOKIE_SECURE = True  # Ensure session cookie is sent over HTTPS
    X_FRAME_OPTIONS = 'DENY'  # Prevent embedding in iframes

# Environment-specific secret settings (optional)
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')  # Change this in production
