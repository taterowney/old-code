#! /bin/bash
cd /
sudo mount /dev/sda1 2> /dev/null
sudo rm -r /media/pi/KINGSTON/TatesBackup/projects/
sudo cp -r /home/pi/projects /media/pi/KINGSTON/TatesBackup/
cd ~
