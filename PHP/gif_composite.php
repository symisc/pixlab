<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Composite a static image on top of a this GIF which should be displayed starting from the frame number 5
# If you want to composite multiple images, the use the 'merge' command instead.

# https://pixlab.io/#/cmd?id=gifcomposite

$gif = 'http://i.stack.imgur.com/h8Hjm.gif';
# Static images to be displayed starting from frame 5
$static = 'http://i.stack.imgur.com/WFr1K.png';

$pix = new Pixlab('My_Pix_Key');

if( !$pix->get('gifcomposite',[
	'img' => $gif,
	'composite' => $static,
    'x' => 10,
	'y' => 30,
	'frame' => 5, #Display the result starting from frame number 5
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "GIF Location: ".$pix->json->link."\n";
?>
