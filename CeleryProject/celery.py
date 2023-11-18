import os
from django.conf import settings

from celery import Celery
from CeleryTest.schedule import tasks_schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')

app = Celery('CeleryProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = tasks_schedule


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
