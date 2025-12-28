import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training_tracker.settings')

app = Celery('training_tracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

app.conf.result_backend = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

app.conf.beat_schedule = {

}