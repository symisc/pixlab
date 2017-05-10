<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Extract Jeremy's face. The rectangle coordinates were obtained from the facedetect command and passed untouched to this command. 
 * Refer to https://pixlab.io/#/cmd?id=crop for additional information.
 */
# Your PixLab key
$key = 'My_Pix_Key';

$pix = new Pixlab($key);
if( !$pix->get('crop',array(
		'img' => 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg',
		'key' => $key,
		"x" => 164,
		"y" => 95,
		"width" => 145,
		"height" => 145
	)) ){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";
?>
