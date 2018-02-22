#!/usr/bin/env python

from django.core.management.base import BaseCommand

from celery import Celery

class Command(BaseCommand):
    def handle(self, *args, **options):
        app = Celery('awx')
        app.config_from_object('django.conf:settings', namespace='CELERY')

        while True:
            print app.control.inspect().active_queues()
            app.control.pool_grow(1)
