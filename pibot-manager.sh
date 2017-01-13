#!/bin/bash
#v0.6.3

wifi=$(ifconfig wlan0 | head -n 4 | tail -n 1 | cut -d ' ' -f 13)
dns=$(ping -c 1 google.com | tail -n 2 | head -n 1 | cut -d ',' -f 2 | cut -d ' ' -f 2)
ip=$(ping -c 1 8.8.8.8 | tail -n 2 | head -n 1 | cut -d ',' -f 2 | cut -d ' ' -f 2)
connected="true"

if [ $wifi != "RUNNING" ]
then
echo "[ERROR] WiFi not connected! Program terminating..."
exit 1
fi

if [ $ip != "1" ]
then
echo "[ERROR] No internet connection avaliable! Using local LAN."
connected="false"
fi

if [ $dns != "1" ]
then
echo "[ERROR] DNS Ping test failed! Using local LAN."
fi

if [ $connected == "true" ]
then
echo "[INFO] Attempting to get software upgrades..."
mkdir /tmp/pibot_update
wget http://jplp.tk/repository/projects/pibot/latest.inf -O /tmp/pibot_update/latest.inf
latest=$(cat /tmp/pibot_update/latest.inf | head -n 1)
current=$(cat /home/pi/.pibot/current.inf | head -n 1)
if [ $latest != $current ]
then
echo "[INFO] Update found! Version '$latest'. Updating..."
dll=$(cat /tmp/pibot_update/latest.inf | head -n 2)
wget $dll -O /tmp/pibot_update/update.sh
bash /tmp/pibot_update/update.sh
cp /tmp/pibot_update/latest.inf /home/pi/.pibot/current.inf
rm -r /tmp/pibot_update
echo "[INFO] Update complete! Rebooting in 3 seconds..."
sleep 3
#reboot
fi
else
rm -r /tmp/pibot_update
echo "[INFO] Software is up to date!"
fi

echo "[INFO] Launching WebUI server..."
echo "[INFO] Launching low-level uplink server..."
echo "Goodbye ;)"

screen -dmS pibot-server python /home/pi/.pibot/pibot-server.py
screen -dmS pibot-sensor /home/pi/.pibot/sensors.sh
