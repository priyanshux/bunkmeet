# Bunkmeet — A Proxy Bot
Bunkmeet is a proxy bot who can act as your substitute and attend online meetings / classes hosted on Microsoft Teams.

![Bunkmeet](https://github.com/priyanshux/bunkmeet/blob/main/bunkmeet/static/images/readme.png?raw=true "Bunkmeet")

## Table of Contents
#### 1.  Installation
#### 2.  Components and How To Use
#### 3.  Frequently Asked Quesitons (FAQs)

## Installation

#### Step 0 - Cloning the repository
`git clone https://github.com/priyanshux/bunkmeet`

`cd bunkmeet`

`sudo chmod 755 ubuntu.sh install.sh server.sh worker.sh`

#### Step 1 - Installing required packages
##### Ubuntu/Debian
The installation on Ubuntu/Debian is pretty straightforward.

`./ubuntu.sh`


##### Arch Linux
Install prerequisites for chromedriver along with some Python and Redis packages:

`pacman -Syy`

`sudo pacman -S unzip xvfb libxi6 libgconf-2-4 google-chrome-stable`

`wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip`

`unzip chromedriver_linux64.zip`

Moving chromedriver to `/usr/bin/chromedriver` is important as this is selenium webdriver's executable path. (Default path)

`sudo mv chromedriver /usr/bin/chromedriver`

`sudo chmod 755 /usr/bin/chromedriver`

`rm chromedriver_linux64.zip`

`sudo pacman -S python3 python3-pip python3-venv redis-server`

##### Other Linux distributions

Manually install `chromedriver`, `xvfb` and related packages and move `chromedriver` to `/usr/bin/chromedriver`.

Also install `python3`, `python3-pip`, `python3-venv` and `redis-server`.

#### Step 2 - Running script for pip packages

`./install.sh`

Note that you need to be in the first bunkmeet directory before running these scripts as they are path dependent. Running `./bunkmeet/install.sh` will throw errors.

