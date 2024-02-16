from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-labn(gcq4@&)-ar%xq_8oh4fk)^z6l64y#cyr&eq2#rlh_a6n3"
# SECRET_KEY = str(os.getenv('SECRET_KEY'))
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
