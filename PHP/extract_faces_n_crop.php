<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";


/*  Detect all human faces present in a given image via 'facedetect' and extract each one of them via 'crop'.
 */ 

# Target Image: Feel free to change to whatever image you want
$img = 'https://i.redd.it/oetdn9wc13by.jpg';
# Your PixLab key
$key = 'My_Pix_Key';

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
	echo "Extracting faces...\n";
	foreach($faces as $face){
		/* Invoke crop */
		if( !$pix->get('crop',array(
			'img' => $img,
			'width'=> $face->width,
			'height'=> $face->height,
			'x'=> $face->left,
			'y'=> $face->top
		))){
			echo $pix->get_error_message();
		}else{
			/* Face ID: $face->face_id */
			echo "Face Link: ".$pix->json->link."\n";
		}
	}
}
?>
