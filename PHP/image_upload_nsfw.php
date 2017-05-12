
<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Upload an image first & detect whether it is Not Suitable for Work (NSFW)
# https://pixlab.io/#/cmd?id=nsfw

# Your PixLab key
$key = 'My_Key';

/* Path for the image to upload */
$img_path = './local_img.png';

/* Process */
$pix = new Pixlab($key);
if( !$pix->post('nsfw',array('key' => $key), $img_path) ){
	echo $pix->get_error_message()."\n";
	die;
}
/* Grab NSFW score */
echo "NSFW score: ".$pix->json->score."\n";

?>
