<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Removes a region of an image and collapses the image to occupy the removed portion.
 * https://pixlab.io/#/cmd?id=chop for more info.
 */
# Your PixLab key
$key = 'My_Pix_Key';

$pix = new Pixlab($key);
if( !$pix->get('chop',array(
		'img' => 'http://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
		'height' => 20,
		'x' => 45,
		'y' => 72
	))){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";
?>
