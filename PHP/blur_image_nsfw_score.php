<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Target Image: Change to any link (Possibly adult) you want or switch to POST if you want to upload your image directly, refer to the sample set for more info.
# The target API endpoint we'll be using here: nsfw (https://pixlab.io/cmd?id=nsfw).
$img = 'https://i.redd.it/oetdn9wc13by.jpg';

# Your PixLab API key
$key = 'PIXLAB_API_KEY';

# Censor an image based according to its NSFW score
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
	echo "Censoring NSFW picture...\n";
	/* Call blur with the highest possible radius and sigma */
	if( !$pix->get('blur',array('img' => $img,'rad' => 50,'sig' =>30)) ){
		echo $pix->get_error_message();
	}else{
		echo "Blurred Picture URL: ".$pix->json->link."\n";
	}
}
?>
