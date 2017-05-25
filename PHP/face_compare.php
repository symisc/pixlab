<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";


# Check whether the given faces belong to the same person or not.
# https://pixlab.io/#/cmd?id=facecompare for additional information.
$src = 'https://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg';
$target = 'https://static01.nyt.com/images/2011/07/31/sunday-review/FACES/FACES-jumbo.jpg';

# Unrelated face
#target = 'https://s-media-cache-ak0.pinimg.com/736x/60/aa/e4/60aae45858ab6ce9dc5b33cc2e69baf7.jpg'

# Your PixLab key
$key = 'My_Pix_Key';

/* Verify */
$pix = new Pixlab($key);
/* Create the image first */
if( !$pix->get('facecompare',[
	'src'    => $src,
	'target' => $target,
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}

echo "Same Face?: ". ($pix->json->same_face?'True':'False') ."\n";
echo "Confidence: ". $pix->json->confidence."\n";

?>
