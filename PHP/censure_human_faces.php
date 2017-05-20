<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";


/* Censure all human faces present in a given image by invoking 'facedetect' first which return the rectangle coordinates 
 * of all human faces present & then invoke 'mogrify' to censure those faces.
 */ 

# Target Image: Feel free to change to whatever image you want
$img = 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg';
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
	echo "Censuring faces...\n";
	/* Call mogrify (Only POST) */
	if( !$pix->post('mogrify',array('img' => $img,'cord' => $faces)) ){
		echo $pix->get_error_message();
	}else{
		echo "Censured Faces: ".$pix->json->link."\n";
	}
}
?>
