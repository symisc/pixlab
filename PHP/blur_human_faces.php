<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Detect all human faces in a given image via `facedetect` and blur all of them via `mogrify`.
# https://pixlab.io/cmd?id=facedetect & https://pixlab.io/cmd?id=mogrify for additional information.

# Target Image we want to blur face(s) on
$img = 'https://pixlab.io/images/m3.jpg';
# Your PixLab API key
$key = 'PIXLAB_API_KEY';

$pix = new Pixlab($key);
echo "Detecting faces first...\n";
/* Invoke facedetect first  */
if( !$pix->get('facedetect',array('img' => $img)) ){
	echo $pix->get_error_message();
	die;
}
/* Grab the total number of detected faces */
$faces = $pix->json->faces;
echo "Total number of detected faces: ".count($faces)."\n";

if( count($faces) < 1 ){
	echo "No human faces were were detected on this picture\n";
}else{
	echo "Blurring faces...\n";
	/* Call mogrify (Only POST) */
	if( !$pix->post('mogrify', ['img' => $img,'cord' => $faces]) ){
		echo $pix->get_error_message();
	}else{
		echo "Blurred faces URL: ".$pix->json->link."\n";
	}
}
?>
