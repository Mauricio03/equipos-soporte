# config/default.py

from os.path import abspath, dirname


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = 'de293e2cc24b1023b332a6b3e4c14eaa9eeff25c'

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = '10.68.174.11'
MAIL_PORT = 25
#MAIL_USERNAME = 'user'
#MAIL_PASSWORD = 'pass'
DONT_REPLY_FROM_EMAIL = 'no-reply-soporte-equipos@sva.antel.com.uy'
ADMINS = ('msosachocho@mail.antel.com.uy', )
MAIL_INFORME = 'plataformadeservicios@mail.antel.com.uy'
MAIL_USE_TLS = False
MAIL_DEBUG = False
