import dj_database_url
from todoist.settings.base import *
from todoist.settings.packages.mailhog import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-e1jb$w%@5d^3&lv%0@r@ccu+gkv())12a&obao#wzqtcaqrn9_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "5787-102-88-33-36.ngrok-free.app"]

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR}.db", conn_max_age=600,
)

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# if not DEBUG:
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_ROOT = BASE_DIR / "assets"