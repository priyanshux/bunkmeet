# Bunkmeet — A Proxy Bot
Bunkmeet is an easy-to-use user-friendly proxy bot who can act as your substitute and attend online meetings or classes hosted on Microsoft Teams.

![Bunkmeet](https://github.com/priyanshux/bunkmeet/blob/media/images/readme.png?raw=true "Bunkmeet")

![Worker](https://github.com/priyanshux/bunkmeet/blob/media/images/worker.png?raw=true "Worker")

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

- None of your data (user credentials and team names) is stored anywhere on cloud. Your data is stored locally on your computer at `bunkmeet/database.db` and only you can access it.

- As stressed earlier, running `./bunkmeet/server.sh` or `./bunkmeet/worker.sh` will throw errors. You need to `cd` into the first bunkmeet directory using `cd bunkmeet` before running any of these scripts.

- You can send multiple tasks, but the worker executes the tasks on first come first serve basis. Make sure you send the task to attend an 8AM lecture before the task for 10AM and so on.

- The worker and server are separate and don't depend on each other. You don't need to run both `./server.sh` and `./worker.sh` together for Bunkmeet to work.

- You can run only the server to send a task, close the server and run the worker anytime before your first lecture starts.

- It is, however, recommended to keep the worker running while sending a task to confirm its proper functionality in real-time.

## Quick Ubuntu/Debian Recap

It only takes 3 commands to install and run Bunkmeet on Ubuntu/Debian:

`./ubuntu.sh && ./pip.sh`

 `./server.sh`  on terminal 1

`./worker.sh` on terminal 2

## Experimental Features

Note that you do not need to install any of these features and are optional. Additionally, these features can potentionally show bugs.

### Running the worker headless

Install `supervisor` on your system.

Ubuntu/Debian users can do so using `sudo apt-get install supervisor`

Make sure you're in the first Bunkmeet directory and run the following commands to set up Celery on Supervisor

`sudo bunkmeet=$(pwd) && mkdir $bunkmeet/logs && touch $bunkmeet/logs/worker.out.log && touch $bunkmeet/logs/worker.err.log`

`echo "[program:celery]\ncommand = $bunkmeet/venv/bin/celery -A bunkmeet.routes.celery worker --loglevel=info --without-gossip -P solo\ndirectory = $bunkmeet\nstdout_logfile = $bunkmeet/logs/worker.out.log\nstderr_logfile = $bunkmeet/logs/worker.out.log\nautostart=true\nautorestart = true\nstartsecs = 10\nstopwaitsecs = 600\nstopasgroup=true\npriority=1000" > temp_celery.conf`

`sudo mv temp_celery.conf /etc/supervisor/conf.d/celery.conf && supervisorctl reload`

Now go to `bunkmeet/two.py` and uncomment the following<br>
`# options.binary_location = "/usr/bin/google-chrome-stable"`<br>
`# options.add_argument("--no-sandbox")`<br>
`# options.add_argument("--headless")`<br>
`# options.add_argument("--disable-dev-shm-usage")`<br>
`# driver.set_window_size(1280, 1440)`

This should set up your worker in headless mode.
