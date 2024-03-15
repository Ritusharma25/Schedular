from celery import Celery
from celery import crontab
from .tasks import scrape_proxies

app=Celery('assessment')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scrape_every_day' : { 'task' : 'schedule.tasks.scrape_proxies',
                          'schedule': crontab(minute=00,hour=00), 
                        #   To set schedule timing from here
                          }
}