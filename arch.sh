#!/bin/bash

sudo pacman -Syu

yay -S --nocleanmenu --nodiffmenu --noeditmenu --noupgrademenu --nodevel --norebuild unzip xorg-server-xvfb libxi gconf lib32-gconf google-chrome

#Check the latest chrome driver available for the installed google-chrome-stable
#For more information, see : https://chromedriver.chromium.org/downloads/version-selection
chrome_version=$(/usr/bin/google-chrome-stable --version | grep -Eoh '[0-9,.]+')
echo "Chrome Version : $chrome_version "

a=( ${chrome_version//./ } )                   # replace points, split into array
chrome_version="${a[0]}.${a[1]}.${a[2]}"       # compose new version

latest_release_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version"
latest_release=$(curl $latest_release_url)
echo "Chrome Driver Version : $latest_release"

# Fetch the latest chromedriver
wget http://chromedriver.storage.googleapis.com/$latest_release/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver

sudo chmod 755 /usr/bin/chromedriver

rm chromedriver_linux64.zip

yay -S --nocleanmenu --nodiffmenu --noeditmenu --noupgrademenu --nodevel --norebuild python python-pip python-virtualenv redis postgresql-libs
sudo systemctl enable redis.service
sudo systemctl start redis.service
