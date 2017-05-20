<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Generate GIF from a set of static image
# https://pixlab.io/#/cmd?id=makegif


# Your PixLab key
$key = '335acbd926c0c5c7b80d2c093cc063d3';

/* Process */
$pix = new Pixlab($key);
if( !$pix->post('makegif',array('frames' => [	
		["img" => "https://cdn1.iconfinder.com/data/icons/human-6/48/266-512.png"],	
		["img" => "https://cdn1.iconfinder.com/data/icons/human-6/48/267-512.png"],
		["img" => "https://cdn1.iconfinder.com/data/icons/human-6/48/278-512.png"],	
		["img" => "https://cdn1.iconfinder.com/data/icons/human-6/48/279-512.png"]
		])) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "GIF Link: ".$pix->json->link."\n";
?>
