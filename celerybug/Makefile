celery:
	celery worker -A celerybug -l DEBUG -B -Ofair --autoscale=100,4 -Q tower --pidfile /tmp/celery_pid
	#-n celery@$(COMPOSE_HOST)

