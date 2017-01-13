#!/bin/bash
#v0.7

echo "[INFO][UPDATER] downloading update..."
rm /home/pi/.pibot/pibot-server.py
rm /home/pi/.pibot/pibot-manager.sh
echo "inuse" > current.inf
cd /home/pi/.pibot/
wget -q http://68.187.116.243/repository/projects/pibot/beta/v0.7/core/pibot-server.py
wget -q http://68.187.116.243/repository/projects/pibot/beta/v0.7/manager/pibot-manager.sh
cd /var/www/html/control/
wget -qr http://68.187.116.243/repository/projects/pibot/beta/v0.7/webui/
exit 0
