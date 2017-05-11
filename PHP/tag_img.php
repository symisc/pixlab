<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Tag an image based on detected visual content which mean running a CNN on top of it.
# https://pixlab.io/#/cmd?id=tagimg for more info.

# Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the sample set for more info.
$img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg';
# Your PixLab key
$key = 'My_Pixlab_Key';
/* Process */
$pix = new Pixlab($key);
if( !$pix->get('tagimg',array(
	'img' => $img,
	'key' => $key
	)) ){
	echo $pix->get_error_message();
	die;
}
/* Grab the total number of tags */
$tags = $pix->json->tags;
echo "Total number of detected tags: ".count($tags)."\n";
foreach($tags as $tag){
	echo "Tag = ".$tag->name.", Confidence: ".$tag->confidence."\n";
}
