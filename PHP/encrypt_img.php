<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Converts plain pixels of a given image to enciphered pixels. The image is not readable until it has been deciphered using decrypt.
# https://pixlab.io/#/cmd?id=encrypt && https://pixlab.io/#/cmd?id=decrypt

# Target image to enrypt
$img = 'https://pixlab.io/images/bencrypt.png';
# Password used for decryption
$pwd = 'superpass';

$pix = new Pixlab('My_Pix_Key');
/* Grab the face landmarks first */
if( !$pix->get('encrypt',[
	'img' => $img,
	'pwd' => $pwd
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Link to the encrypted picture: ".$pix->json->link."\n";
# Call https://api.pixlab.io/decrypt with your passphrase to make it readable again
?>
