# Django settings for speedycomputers project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('edilio', 'edilio73@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'cubanoshaciacuba'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'whatever'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3306'              # Set to empty string for default. Not used with sqlite3.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cubanoshaciacuba',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'whatever',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/html/wmedia/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/wmedia/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!enoiltu93o6%ier+y^*zf9z#ie12x0+s5ozkhdf3)qwg%-*r)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'cubanoshaciamiami.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/var/www/html/websites/cubanoshaciamiami/templates/",
     "/var/www/html/websites/cubanoshaciamiami/templates/services/",
     "/var/www/html/websites/cubanoshaciamiami/templates/adaptacion/",
     "/var/www/html/websites/cubanoshaciamiami/templates/estabilidad/",
     "/var/www/html/websites/cubanoshaciamiami/templates/presupuesto/"

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'cubanoshaciamiami.services',
    'cubanoshaciamiami.ayudamemoria',
    'cubanoshaciamiami.presupuesto',
    #'cubanoshaciamiami.django_monetize',
)

MONETIZE_DEFAULT = (
    'django_monetize/amazon_search.html',
    ('amazon_search_terms','Django book'),
    ('amazon_search_title','Search for Django books!')
)

MONETIZE_TARGET = {
    'django':'django_monetize/paypal_donate.html',
    'Author (Will Larson)':'django_monetize/amazon_honor.html',
    'Author (Joe Somebody)':(
        'django_monetize/amazon_honor.html',
        ('amazon_paypage','Joe Somebodys Amazon Honor Paypage url'),
    ),
    'tutorial':{
        'header':'django_monetize/paypal_donate.html',
        'footer':'django_monetize/amazon_omakase.html',
        None:(
            'django_monetize/amazon_search.html',
            ('amazon_search_terms','JQuery'),
            ('amazon_search_title','Buy books on JQuery!'),
        ),
    },
}

MONETIZE_CONTEXT = {
    'amazon_affiliates_id':'your affiliates tracking id',
    'amazon_paypage':'default amazon paypages url',
    'paypal_business':'edilio73@gmail.com',
    'paypal_item_name':'www.cubanoshaciamiami.com',
    'paypal_currency_code':'USD',
    'paypal_tax':'0',
    'paypal_lc':'US',
    'paypal_bn':'PP-DonationsBF',
    'paypal_image':'http://www.paypal.com/en_US/i/btn/btn_donate_LG.gif',
}


#DEFAULT_CHARSET = "windows-1252"