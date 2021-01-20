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

#### Arch Linux

Make sure you have the following dependencies: `alsa-lib`, `gtk3`, `libcups`, `libxss`, `libxtst`, ` nss`, `google-chrome`, `xdg-utils` before installing `chromedriver` from AUR using

`git clone https://aur.archlinux.org/chromedriver.git`

`cd chromedriver`

`makepkg -si`

`chromedriver` should be in `/usr/bin/` (Important)

Install Python, Pip, Venv and Redis packages if you don't have them already:

`sudo pacman -S python3 python3-pip python3-venv redis-server`

#### Other Linux distributions

Manually install `chromedriver`, its dependencies and move `chromedriver` to `/usr/bin/chromedriver`.

Also install `python3`, `python3-pip`, `python3-venv` and `redis-server`.

### Step 2 - Running script for pip packages

`./pip.sh`

Note that you need to be in the first bunkmeet directory before running these scripts as they are path dependent. Running `./bunkmeet/pip.sh` will throw errors.

## Components and How To Use

![Components](https://github.com/priyanshux/bunkmeet/blob/media/images/worker.png?raw=true "Components")
