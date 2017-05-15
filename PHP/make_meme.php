<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Draw some funny text on top & button of the famous Michael Jordan crying face.
# https://pixlab.io/#/cmd?id=drawtext is the target command

/* Target image */
$img = 'https://pixlab.io/images/jdr.jpg';

# Your PixLab key
$key = 'My_Pix_Key';

/* Process */
$pix = new Pixlab($key);
if( !$pix->get('drawtext',array(
			'img' => $img,
			'top' => 'someone bumps the table',
			'bottom' => 'right before you win',
			'cap' => true, # Capitalize text,
			'strokecolor' => 'black'
		)) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Pic Link: ".$pix->json->link."\n";

?>
