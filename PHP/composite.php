<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
/*
 * Composite two smiley on top of the famous Michael jordan crying face.
 * A more sophisticated approach would be to extract the face landmarks using facelandmarks and composite something on the different regions.
 * https://pixlab.io/#/cmd?id=merge for more info.
 */
# Your PixLab key
$key = 'MY_Pix_Key';

$pix = new Pixlab($key);
if( !$pix->post('merge',array(
		'src' => 'https://pbs.twimg.com/media/CcEfpp0W4AEQVPf.jpg',
		'cord'=>[
		[
		   'img' => 'http://www.wowpng.com/wp-content/uploads/2016/10/lol-troll-face-png-image-october-2016-370x297.png',
		   'x' => 30,
		   'y' => 320
		],
		[
		   'img' => 'http://orig08.deviantart.net/67d1/f/2010/216/6/7/lol_face_by_bloodyhalfdemon.png',
		   'x' => 630,
		   'y' => 95
		]],
		'key' => $key
	))){
	echo $pix->get_error_message();
	die;
}
echo "Pic Link: ".$pix->json->link."\n";
?>
