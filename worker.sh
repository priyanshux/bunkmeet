#!/bin/bash

source venv/bin/activate

celery -A bunkmeet.routes.celery worker --loglevel=info