#!/bin/bash

CPU_USE=0
CPU_TEMP=0
WIFI_RSSI=0
GEN_WARN="on"

while true
do
    idle=$(iostat | head -n 4 | tail -n 1 | cut -d ' ' -f 30 | cut -d '.' -f 1)
    CPU_USE=$(expr 100 - $idle)
    CPU_TEMP=$(/opt/vc/bin/vcgencmd measure_temp | cut -d '=' -f 2 | cut -d '.' -f 1)
    WIFI_RSSI=$(qual=$(iwconfig | grep Quality | cut -d '=' -f 2 | cut -d ' ' -f 1 | bc -l) && qual=$(echo "$qual*100" | bc | cut -d '.' -f 1) && echo "$qual/20" | bc)
    if [[ $(ps a | grep python | head -n 1 | cut -d ' ' -f 11) -ne "python" ]]
    then
    GEN_WARN="on"
    fi

    echo $CPU_USE > /var/www/uplink/cpuuse
    echo $CPU_TEMP > /var/www/uplink/cputemp
    echo $WIFI_RSSI > /var/www/uplink/rssi
    echo $GEN_WARN > /var/www/uplink/genwarn
    echo $CPU_USE
    echo $CPU_TEMP
    echo $WIFI_RSSI
    echo $GEN_WARN
    sleep 1s
done 