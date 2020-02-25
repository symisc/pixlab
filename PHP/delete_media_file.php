<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Remove a previously stored media file. All your processed media files are stored by default on pixlab.xyz unless you set your own AWS S3 key (refer to your dashboard on how to do that). In which case, everything shall be stored on your own S3 bucket.
 * Refer to https://pixlab.io/cmd?id=delete for more info.
 */
# Your PixLab key
$key = 'My_Pixlab_Key';

$pix = new Pixlab($key);
if( !$pix->get('delete',array(
		'link'=>'http://media.pixlab.xyz/24p5e554681b9884.png'
	))){
	echo $pix->get_error_message();
	die;
}
echo "Deletion succeed";

?>
