# This file contains sensitive data.
# The DATABASE and SECRET_KEY in production are different.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ss4jgn&zv9(c@h81^9rie7*#s6=o@lr2z#0x*ycg@i=&1_qc1&'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}