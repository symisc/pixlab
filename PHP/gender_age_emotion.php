<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Detect all human faces present in a given image and try to guess their age, gender and emotion state via their facial shapes.
# https://pixlab.io/#/cmd?id=facemotion for more info.

# Target Image: Feel free to change to whatever image holding as many human faces as you want.
$img = 'http://www.scienceforums.com/uploads/1282315190/gallery_1625_35_9165.jpg';

# Your PixLab key
$key = 'My_Pixlab_Key';
/* Analyze */
$pix = new Pixlab($key);
if( !$pix->get('facemotion',array(
	'img' => $img
	)) ){
	echo $pix->get_error_message();
	die;
}
/* Grab the total number of detected faces */
$faces = $pix->json->faces;
echo "Total number of detected faces: ".count($faces)."\n";
if( count($faces) < 1 ){
	echo "No human faces were were detected on this picture\n";
}else{
	# Iterate all over the detected faces
	foreach($faces as $face){
		$coord = $face->rectangle;
		echo 'Face coordinate: width: ' . $coord->width . ' height: ' . $coord->height . ' X: ' . $coord->left . ' Y: ' . $coord->top . "\n";
		# Guess emotion
		foreach( $face->emotion as $emotion ){
			if ( $emotion->score > 0.5 ){
				echo "Emotion - " . $emotion->state. ': ' . $emotion->score. "\n";
			}
		}
		# Grab the age and gender
		echo "Age ~: " . $face->age. "\n";
		echo "Gender: " . $face->gender . "\n";
	}
}
?>
