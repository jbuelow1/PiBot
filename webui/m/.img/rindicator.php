<?php
$root = "/var/www/uplink/";

echo "<head><meta http-equiv=\"refresh\" content=\"1\"></head>";

$gimspeed = file_get_contents($root . "gimspeed");
$manspeed = file_get_contents($root . "manspeed");
$gimhome = file_get_contents($root . "gimhome");
$manclaw = file_get_contents($root . "manclaw");
$manhome = file_get_contents($root . "manhome");

$gimspeed = str_replace(array("\r", "\n"), '', $gimspeed);
$manspeed = str_replace(array("\r", "\n"), '', $manspeed);
$gimhome = str_replace(array("\r", "\n"), '', $gimhome);
$manclaw = str_replace(array("\r", "\n"), '', $manclaw);
$manhome = str_replace(array("\r", "\n"), '', $manhome);

echo "<progress value=\"" . $gimspeed . "\" max=\"10\" style=\"width:100%;border:2px solid;\"></progress>";
echo "<pre>^    Gimbal Speed   ^</pre>";
echo "<progress value=\"" . $manspeed . "\" max=\"10\" style=\"width:100%;border:2px solid;\"></progress>";
echo "<pre>^ Manipulator Speed ^</pre>";
echo "<center><img src=\"home_" . $gimhome . ".png\" height=\"25%\" style=\"float:left;\" alt=\"Gimbal Home Status\">";
echo "<img src=\"claw_" . $manclaw . ".png\" height=\"25%\" style=\"float:;\" alt=\"Manipulator Claw Status\">";
echo "<img src=\"home_" . $manhome . ".png\" height=\"25%\" style=\"float:right;\" alt=\"Manipulator Home Status\"></center>";
?>