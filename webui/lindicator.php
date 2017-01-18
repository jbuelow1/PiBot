<?php
$root = "/var/www/uplink/";

echo "<head><meta http-equiv=\"refresh\" content=\"1\"></head>";

$movspeed = file_get_contents($root . "movspeed");
$genwarn = file_get_contents($root . "genwarn");
$rssi = file_get_contents($root . "rssi");
$cpuuse = file_get_contents($root . "cpuuse");
$cputemp = file_get_contents($root . "cputemp");
$prox = file_get_contents($root . "prox");

$movspeed = str_replace(array("\r", "\n"), '', $movspeed);
$genwarn = str_replace(array("\r", "\n"), '', $genwarn);
$rssi = str_replace(array("\r", "\n"), '', $rssi);
$cpuuse = str_replace(array("\r", "\n"), '', $cpuuse);
$cputemp = str_replace(array("\r", "\n"), '', $cputemp);
$prox = str_replace(array("\r", "\n"), '', $prox);

echo "<progress value=\"" . $movspeed . "\" max=\"10\" style=\"width:100%;border:2px solid;\"></progress>";
echo "<pre>^ Movement Speed ^</pre>";
echo "<img src=\"warn_" . $genwarn . ".png\" height=\"25%\" alt=\"General Alert\">";
echo "<img src=\"signal_" . $rssi . ".gif\" height=\"25%\" style=\"float:right;\" alt=\"WiFi RSSI\">";
echo "<br><pre>PROX: " . $prox . "<br>USAGE: " . $cpuuse . "<br>TEMP: " . $cputemp . "</pre>";
?>