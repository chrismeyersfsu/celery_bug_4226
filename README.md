```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

* install rabbitmq and start it
* update celerybug/celerybug/settings.py with rabbit connection info
* `cd celerybug`
* start celery via `make celery`
* invoke bug via `make bug`
