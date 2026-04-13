INSTALLED_APPS = [
    ...,
    'rest_framework',
    'etudiants',
]

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['*']
DATABASE_URL = 'postgresql://collecte_user:LRl03YV6T6SkcC0oK2kyIpYyCTJ8RC2w@dpg-d7ebetjbc2fs73efv6d0-a/collecte'

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}