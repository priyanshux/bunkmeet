#!/bin/bash

bunkmeet=$(pwd)

python3 -m venv $bunkmeet/venv 

source venv/bin/activate

pip3 install -r requirements.txt

pip3 install flask

pip3 install -U "celery[redis]"