#!/bin/bash
#v0.7

echo "[INFO][UPDATER] downloading update..."
rm -r /home/pi/.pibot
rm -r /var/www/html/control/*
echo "inuse" > current.inf
cd /tmp/pibot_update
git clone https://github.com/jbuelow1/PiBot.git
cd PiBot
git checkout v1.0
mkdir /PiBotOS
cp ./core/pibot-server.py /PiBotOS/server.py
cp ./core/sensors.sh /PiBotOS/sensors.sh
cp ./manager/pibot-manager.sh /PiBotOS/start.sh
cp -r ./webui/* /var/www/html/control/

