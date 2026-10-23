import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de Segurança e Ambiente
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-chave-provisoria-hugel-manner')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'andersonewald.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]
# Permite adicionar hosts dinamicamente via arquivo .env na VPS
if os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS.extend(os.getenv('ALLOWED_HOSTS').split(','))

# Aplicações instaladas no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Seus aplicativos customizados
    'apps.institucional.apps.InstitucionalConfig',    
    'apps.blog',
    'apps.agenda',
    'apps.parceiros',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # 🌟 Suporte a arquivos estáticos na VPS
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # Middleware para interceptar o clique nas bandeiras e mudar o idioma
    'django.middleware.locale.LocaleMiddleware', 
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Caminho para os templates
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

WSGI_APPLICATION = 'core_project.wsgi.application'

# Base de Dados MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'hugel_db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'PnCdEL'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Configurações de Idioma e Fuso Horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('pt-br', 'Português'),
    ('de', 'Deutsch'),
    ('en', 'English'),
    ('es', 'Español'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Configuração de Arquivos Estáticos (CSS, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 🌟 ADICIONADO: Pasta onde o collectstatic reunirá os arquivos estáticos na VPS
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuração de Upload de Imagens
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de E-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'hugelmannerplattler@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'jodmsdjbvduqrmsf')