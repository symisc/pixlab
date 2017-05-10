<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Generate a border with a desired color for a given image.
 * https://pixlab.io/#/cmd?id=border for more info.
 */
# Your PixLab key
$key = '335acbd926c0c5c7b80d2c093cc063d3';

$pix = new Pixlab($key);
if( !$pix->get('border',array(
		'img'   => 'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
		'width' => 20,
		'color' => 'yellow',
		'key' => $key
	))){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";
?>
