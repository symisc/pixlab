<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Find a person's face in a crowd or group of people. https://pixlab.io/#/cmd?id=facelookup for additional information.

# This is the target face that we are searching for in the people crowd.
$face = 'http://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg';
# The people crowd to look on
$crowd = 'http://www.acclaimimages.com/_gallery/_free_images/0519-0908-1001-0556_president_barack_obama_walking_with_a_crowd_of_people_o.jpg';

$pix = new Pixlab('My_Pix_Key');

if( !$pix->get('facelookup',[
	'face' => $face,
	'crowd' => $crowd,
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
$found = $pix->json->found; # Boolean value telling whether we got the face or not
if ($found){
	echo "Face found with confidence value = ". $pix->json->confidence;
	$rectangle = $pix->json->rectangle; # Rectangle coordinates of the target face
	echo "\nFace Coordinates: top: ".$rectangle->top." left: ".$rectangle->left." width: ".$rectangle->width." height:".$rectangle->height."\n";
}else{
	echo "Face NOT found in the target crowd..picking up the best candidate:\n";
	$best = $pix->json->best;
	$rectangle = $best->rectangle; # Rectangle coordinates of the best candidate
	echo "Confidence: ". $best->confidence;
	echo "\nBest Candidate Coordinates: top: ".$rectangle->top." left: ".$rectangle->left." width: ".$rectangle->width." height:".$rectangle->height."\n";
}
?>
