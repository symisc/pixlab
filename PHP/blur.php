<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Blur the bird picture
 * Refer to https://pixlab.io/#/cmd?id=blur for more info.
 */
# Your PixLab key
$key = 'My_Pixlab_Key';

$pix = new Pixlab($key);
if( !$pix->get('blur',array(
		'img'=>'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
		'radius'=>50,
		'sigma'=>30
	))){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";

?>
