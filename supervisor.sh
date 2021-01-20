#!/bin/bash

sudo touch /etc/supervisor/conf.d/celery.conf

sudo mkdir $bunkmeet/logs

sudo touch $bunkmeet/logs/worker.out.log

sudo touch $bunkmeet/logs/worker.err.log

echo "[program:celery]\ncommand = $bunkmeet/venv/bin/celery -A bunkmeet.routes.celery worker --loglevel=info --without-gossip -P solo\ndirectory = $bunkmeet\nstdout_logfile = $bunkmeet/logs/worker.out.log\nstderr_logfile = $bunkmeet/logs/worker.out.log\nautostart=true\nautorestart = true\nstartsecs = 10\nstopwaitsecs = 600\nstopasgroup=true\npriority=1000" > temp_celery.conf

sudo mv temp_celery.conf /etc/supervisor/conf.d/celery.conf

sudo supervisorctl reload
