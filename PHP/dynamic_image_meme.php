<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";


# Dynamically create a 300x300 PNG image with a yellow background and draw some text on top of it later.
# Refer to https://pixlab.io/#/cmd?id=newimage && https://pixlab.io/#/cmd?id=drawtext for additional information.

	
# Your PixLab key
$key = 'My_Pix_Key';

/* Process */
$pix = new Pixlab($key);
echo "Creating new 300x300 PNG image...\n";
/* Create the image first */
if( !$pix->get('newimage',[
	"width" => 300,
	"height" => 300,
	"color" => "yellow"
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
# Link to the new image
$img = $pix->json->link;

echo "Drawing some text now...\n";
if( !$pix->get('drawtext',[
	'img' => $img, #The newly created image
	"cap" => True, #Uppercase
	"color" => "black", #Text color
	"font" => "wolf",
	"center" => "bonjour"
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "New Pic Link: ".$pix->json->link."\n";
  ?>
