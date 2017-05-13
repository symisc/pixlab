<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Resize an image to half its original size hence the 50% field.
# https://pixlab.io/#/cmd?id=scale for additional information.

/* Target image */
$img = 'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg';

# Your PixLab key
$key = 'My_Pix_Key';

/* Process */
$pix = new Pixlab($key);
if( !$pix->get('scale',array('img' => $img, 'key' => $key, 'scale' => 50 /* Scale percentage */)) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Pic Link: ".$pix->json->link."\n";

?>
