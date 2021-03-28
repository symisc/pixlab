<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Upload a local image to the remote https://pixlab.xyz storage server or your own S3 bucket depending on the configuration on the PixLab dashboard.
# Use the output link for other purposes such as processing via mogrify, drawrectangles, etc. or simply serving content.
# https://pixlab.io/cmd?id=store for more info.

$img_path = './local_media_file.png';

/* Process */
$pix = new Pixlab('My_Pix_Key');

$pix->switch_to_http();  /* Switch to http for fast upload */

if( !$pix->post('store',array('comment' => 'Super Secret Image'),$img_path) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Uploaded Pic Link: ".$pix->json->link."\n";
