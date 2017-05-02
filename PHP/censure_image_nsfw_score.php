<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Target Image: Change to any link (Possibly adult) you want or switch to POST if you want to upload your image directly, refer to the sample set for more info.
$img = 'https://i.redd.it/oetdn9wc13by.jpg';
# Your PixLab key
$key = 'My_Pixlab_Key';

# Censure an image based on its NSFW score
$pix = new Pixlab($key);
/* Invoke NSFW */
if( !$pix->get('nsfw',array('img' => $img)) ){
	echo $pix->get_error_message();
	die;
}
/* Grab the NSFW score */
$score = $pix->json->score;
if( $score < 0.5 ){
	echo "No adult content were detected on this picture\n";
}else{
	echo "Censuring NSFW picture...\n";
	/* Call blur with the highest possible radius and sigma */
	if( !$pix->get('blur',array('img' => $img,'key'=> $key,'rad' => 50,'sig' =>30)) ){
		echo $pix->get_error_message();
	}else{
		echo "Censured Picture: ".$pix->json->link."\n";
	}
}
?>
