<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Convert a given image to gray color model. A grayscale (or graylevel) image is simply one in which the only colors are shades of gray.
 * https://pixlab.io/#/cmd?id=grayscale for additional information.
 */
# Your PixLab key
$key = 'My_Pix_Key';

$pix = new Pixlab($key);
if( !$pix->get('grayscale',array('img' => 'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg')) ){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";
?>
