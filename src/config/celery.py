import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery beat
app.conf.beat_schedule = {
    'create-task-every-2-minute': {
        'task': 'apps.application.tasks.create_order_task',
        'schedule': crontab(minute='*/2')
    },
}