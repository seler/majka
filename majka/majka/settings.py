# -*- coding: utf-8 -*-
# Django settings for majka project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Rafał Selewońko', 'rafal@selewonko.com'),
)

MANAGERS = ADMINS

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '../../bricks_majka.db3',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'majka',
        'USER': 'majka',
        'PASSWORD': '5tgbcde3',
        'HOST': 'wi.selewonko.com',
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl-pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

import os
import manage
PROJECT_PATH = os.path.dirname(manage.__file__)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://majka.wi.selewonko.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://majka.wi.selewonko.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    'layout',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gn^2v*l9w(alc(3fzmh@!r^9)6!w$(cv&amp;erdq=0a57a!je)y@4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'majka.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'majka.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'djcelery',
    'south',
    'tinymce',
    'bricks',
    'bricks.collections',
    'bricks.images',
    'bricks.videos',
    'bricks.articles',
)

import djcelery
djcelery.setup_loader()

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"
BROKER_URL = 'amqp://guest:guest@localhost:5672/'

CELERYD_CONCURRENCY = 1
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_QUEUES = {
    "default": {
        "exchange": "celery",
        "queue_arguments": {"x-ha-policy": "all"},
        "binding_key": "celery"
    },
}

CELERY_DEFAULT_QUEUE = "default"

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}


def gettext(s):
    return s

BRICKS_USE_CELERY = True
BRICK_COLLECTIONS_TEMPLATE_NAME_CHOICES = (
    ("collections/collection_detail.html", gettext(u"default")),
    ("collections/collection_blog.html", gettext(u"blog")),
    ("images/gallery_detail.html", gettext(u"gallery")),
)
BRICKS_ARTICLE_SECTION_DEFAULT = 'text'
BRICKS_ARTICLE_SECTION_TYPES = {
    'text': {
        'name': gettext(u"Text"),
        'template_name': 'articles/sections/text.html',
    },
    'block_divider': {
        'name': gettext(u"Block divider"),
        'template_name': 'articles/sections/block_divider.html',
    },
    'quote_left': {
        'name': gettext(u"Quote (left)"),
        'template_name': 'articles/sections/quote_left.html',
    },
    'quote_right': {
        'name': gettext(u"Quote (right)"),
        'template_name': 'articles/sections/quote_right.html',
    },
    'big_image': {
        'name': gettext(u"Big image"),
        'template_name': 'articles/sections/big_image.html',
        'app_label': 'images',
        'model_name': 'image',
    },
    'video': {
        'name': gettext(u"Video"),
        'template_name': 'articles/sections/video.html',
        'app_label': 'videos',
        'model_name': 'video',
    },
}

FFMPEG = '/usr/bin/ffmpeg'
GREP = '/bin/grep'
GREP = '/bin/grep'
QT_FASTSTART = '/usr/bin/qt-faststart'
BRICKS_ALLOWED_VIDEO_FORMATS = ('3gp', 'avi', 'flv', 'mkv', 'mov', 'm4v', 'mpeg',
                                'mpg', 'ogg', 'ogv', 'wmv', 'mp4')
BRICKS_DEFAULT_CONVERTEDVIDEO_FORMATS = (1, 2)
BRICKS_DEFAULT_CONVERTEDVIDEO_FORMAT = 2

BRICKS_VIDEO_ASPECT_RATIO_CHOICES = (
    (1.33, u'4:3'),
    (1.78, u'16:9')
)

BRICKS_VIDEO_FORMATS = {
    1: {
        'name': '270p',
        'slug': '270p',
        'codec': 'm4v',
        'extension': '.m4v',
        1.78: {'width': 480,
               'height': 270},
        1.33: {'width': 360,
               'height': 270},
        'command': '{ffmpeg} -y -i {filename} -s {format_width}x{format_height} -vcodec libx264 -vpre baseline -vb 300k -r 30  -acodec libfaac -ab 64k -flags +loop+mv4 -cmp 256 -partitions +parti4x4+parti8x8+partp4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -bf 3 -flags2 +bpyramid+wpred+mixed_refs+dct8x8 -coder 1 -me_range 16 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -qmin 10 -qmax 51 -qdiff 4 {format_filename}',
        'fallback': None,
    },

    2: {
        'name': '360p',
        'slug': '360p',
        'codec': 'm4v',
        'extension': '.m4v',
        1.78: {'width': 640,
               'height': 360},
        1.33: {'width': 478,
               'height': 360},
        'command': '{ffmpeg} -y -i {filename} -s {format_width}x{format_height} -vcodec libx264 -vpre baseline -vb 512k -r 30  -acodec libfaac -ab 96k -flags +loop+mv4 -cmp 256 -partitions +parti4x4+parti8x8+partp4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -bf 3 -flags2 +bpyramid+wpred+mixed_refs+dct8x8 -coder 1 -me_range 16 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -qmin 10 -qmax 51 -qdiff 4 {format_filename}',
        'fallback': 1,
    },

    3: {
        'name': '576p',
        'slug': '576p',
        'codec': 'm4v',
        'extension': '.m4v',
        1.78: {'width': 1024,
               'height': 576},
        1.33: {'width': 768,
               'height': 576},
        'command': '{ffmpeg} -y -i {filename} -s {format_width}x{format_height} -vcodec libx264 -vpre baseline -vb 1600k -r 30  -acodec libfaac -ab 112k -flags +loop+mv4 -cmp 256 -partitions +parti4x4+parti8x8+partp4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -bf 3 -flags2 +bpyramid+wpred+mixed_refs+dct8x8 -coder 1 -me_range 16 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -qmin 10 -qmax 51 -qdiff 4 {format_filename}',
        'fallback': 1,
    },
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
