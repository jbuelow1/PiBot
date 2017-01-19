<?php
$file = "/var/www/downlink";
$cont = $_GET['cmd'];
file_put_contents($file, $cont);
print("ok");
?>
