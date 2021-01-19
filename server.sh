#!/bin/bash

source venv/bin/activate

export FLASK_APP=run.py 

flask run --host=localhost