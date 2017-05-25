<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";


# Check if a given image is of the right size: 800x600 and if not try to resize it.
# The command of interest here are header: https://pixlab.io/#/cmd?id=header & smartresize: https://pixlab.io/#/cmd?id=smartresize
$img = 'https://s-media-cache-ak0.pinimg.com/736x/60/aa/e4/60aae45858ab6ce9dc5b33cc2e69baf7.jpg';

$key = 'My_Pix_Key';
# Obtain image metadata at first via header

$pix = new Pixlab($key);

if( !$pix->get('header',[
	"img" => $img
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}

$w = $pix->json->width;
$h =  $pix->json->height;
if ($w > 800 || $h > 600){
	echo "Resizing image from ${w}x${h} to near 800x600...\n";
	# Invoke smart resize...
	if( !$pix->get('smartresize',[
		'img'    => $img,
		'width'  => 800,
		'height' => 600
	]) ){
		echo $pix->get_error_message()."\n";
	}else{
		echo "Resized image: ".$pix->json->link."\n";
	}
}else{
	echo "Uploaded image is of the correct size!\n";
}
?>
