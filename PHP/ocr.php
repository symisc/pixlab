<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Given an image with human readable characters. Detect input language & extract text content from there.
# https://pixlab.io/#/cmd?id=ocr for additional information.

/* Target image with human readable text input */
$img = 'http://quotesten.com/wp-content/uploads/2016/06/Confucius-Quote.jpg';

# Your PixLab key
$key = 'My_PixLab_Key';

/* Process */
$pix = new Pixlab($key);
if( !$pix->get('ocr',array('img' => $img)) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Input language: ".$pix->json->lang;
echo "\nText Output: ".$pix->json->output."\n";

?>
