import os

from celery import Celery

# Загрузка настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Настройки из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматический поиск задач
app.autodiscover_tasks()