from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerybug.settings')

app = Celery('celerybug')
app.config_from_object('django.conf:settings', namespace='CELERY')


'''
app = Celery('celerybug',
             broker='amqp://guest:guest@rabbitmq:5672',
             include=[])
'''

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
