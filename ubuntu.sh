#!/bin/bash

sudo apt-get -y update

sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4 google-chrome-stable

wget http://chromedriver.storage.googleapis.com/98.0.4758.48/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver

sudo chmod 755 /usr/bin/chromedriver

rm chromedriver_linux64.zip

sudo apt install -y python3 python3-pip python3-venv redis-server
