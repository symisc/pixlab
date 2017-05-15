<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

/* Extract a screen capture from a given website */
$website = 'https://sqlite.org';
# Your PixLab key
$key = 'My_Pix_Key';

$pix = new Pixlab($key);
/* Note that you can specify the desired width & height and image export format if you want to. Read the command doc at: https://pixlab.io/#/cmd?id=screencapture for additional info */
if( !$pix->get('screencapture',array('url' => $website)) ){
	echo $pix->get_error_message();
	die;
}
echo "The Website screen capture is located on: ".$pix->json->link."\n";

?>
