#!/bin/sh
# lanucher.sh
# navigate to home directory, then this directory, then execute python script, then back home
cd /
cd home/pi/Robo-Ops
sudo python motor_controller.py
sudo python arm_controller.py
sudo python camera.py
cd /
