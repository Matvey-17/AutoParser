import os 
from celery import Celery 
from celery.schedules import crontab
from core.settings import CELERY_BROKER_URL


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 

app = Celery(
    'core', 
    # broker=CELERY_BROKER_URL, 
    # backend=CELERY_BROKER_URL,
    # include=['currencies.tasks']
) 
app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks() 

app.conf.beat_schedule = {
    'update_jpy_daily': {
        'task': 'currencies.tasks.update_jpy_task',
        # 'schedule': crontab(hour=11, minute=0),  
        'schedule': 30,  
    },
    'update_krw_daily': {
        'task': 'currencies.tasks.update_krw_task',
        # 'schedule': crontab(hour=11, minute=0),
        'schedule': 30,  
    },
    'update_cny_daily': {
        'task': 'currencies.tasks.update_cny_task',
        # 'schedule': crontab(hour=11, minute=0),
        'schedule': 30,  
    },
}