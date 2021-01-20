# Bunkmeet — A Proxy Bot
Bunkmeet is an easy-to-use user-friendly proxy bot who can act as your substitute and attend online meetings or classes hosted on Microsoft Teams.

![Bunkmeet](https://github.com/priyanshux/bunkmeet/blob/media/images/readme.png?raw=true "Bunkmeet")

![Worker](https://github.com/priyanshux/bunkmeet/blob/media/images/worker.png?raw=true "Worker")

## Table of Contents
#### 1.  Installation
#### 2.  Components and How To Use
#### 3.  Frequently Asked Quesitons (FAQs)

## Installation

### Step 0 - Cloning the repository
`git clone https://github.com/priyanshux/bunkmeet`

`cd bunkmeet`

### Step 1 - Installing required packages
#### Ubuntu/Debian
The first step on Ubuntu/Debian is pretty straightforward.

`./ubuntu.sh`

Note that you need to be in the first bunkmeet directory before running these scripts as they are path dependent. Running `./bunkmeet/ubuntu.sh` will throw errors.

#### Other Linux distributions

Manually install `chromedriver`, its dependencies and move `chromedriver` to `/usr/bin/`. The executable path in Bunkmeet's webdriver is `/usr/bin/chromedriver`

Also install `python3`, `python3-pip`, `python3-venv` and `redis-server`.

### Step 2 - Running script for pip packages

`./pip.sh`

Note that you need to be in the first bunkmeet directory before running these scripts as they are path dependent. Running `./bunkmeet/pip.sh` will throw errors.

## Components and How To Use

You need to open two separate terminals and run `./server.sh` and `./worker.sh`

![Components](https://github.com/priyanshux/bunkmeet/blob/media/images/components.png?raw=true "Components")

### Terminal 1

Run `./server.sh` on terminal 1 and go to http://localhost:5000/, you'll be prompted to log in if you're using Bunkmeet for the first time or have deleted data from `bunkmeet/database.db`.

### Terminal 2

Run `./worker.sh`  and do not close until all your tasks (lectures) have been over.

### Note:

- As stressed earlier, running `./bunkmeet/server.sh` or `./bunkmeet/worker.sh` will throw errors. You need to `cd` into the first bunkmeet directory using `cd bunkmeet` before running any of these scripts.

- None of your data (user credentials and team names) is stored anywhere on cloud. Your data is stored locally on your computer at `bunkmeet/database.db` and only you can access it.

- You don't need to run `./worker.sh` before sending tasks. You can ask Bunkmeet (server) to attend a lecture now and run the worker anytime before the lecture starts, but it is recommended to run it before.
