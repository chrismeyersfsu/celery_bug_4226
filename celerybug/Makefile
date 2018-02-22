celery:
	celery worker -A celerybug -l DEBUG -B -Ofair --autoscale=100,4 -Q tower --pidfile /tmp/celery_pid

bug:
	manage.py start_celery_jobs
