from redisxdjango.celery import app
from django.test import Client
from django.core.cache import cache
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@app.task
def reboot_cache_main():
    res = cache.keys('*main*')
    if res:
        time_life = cache.ttl(res[0])
        delete_cache = cache.delete_many(res)
    c = Client()
    response = c.get('/', SERVER_NAME='127.0.0.1:8000')

@app.task
def reboot_cache_main_crontab():
    res = cache.keys('*main*')
    logger.info(f'Check cache')
    if res:
        for id_cache in res:
            time_life = cache.ttl(id_cache)
            logger.info(f'Time to expire {time_life}')
            if time_life is None:
                break
            if time_life > 300:
                return
            break
    logger.info(f'Reload cache')
    c = Client()
    response = c.get('/', SERVER_NAME='127.0.0.1:8000')
