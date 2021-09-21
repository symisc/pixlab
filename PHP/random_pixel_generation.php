<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Generates a set of random pixels of desired Width & Height. 
# This endpoint is similar to the /newimage endpoint except that the image contents is filled with random pixels. 
# This is very useful for generating background (negative) samples for feeding Machine Learning training algorithms.
# https://pixlab.io/cmd?id=pixelgenerate for additonal information.

# Your PixLab API key
$key = 'MY_PIXLAB_API_KEY'; # Get yours from https://console.pixlab.io/

# Randomly generate the Pixel
$pix = new Pixlab($key);
if( !$pix->get('pixelgenerate',[
  "width" => 300,
	"height" => 300
]) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Randomly generated Image: ".$pix->json->ssl_link."\n";
