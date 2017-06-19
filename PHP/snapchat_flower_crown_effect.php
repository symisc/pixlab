<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Detect all human faces & extract their landmark regions via facelandmarks & make a small Snapchat filter effect.
# Only three commands are actually needed in order to mimic the Snapchat filters effects:
# face landmarks:         https://pixlab.io/#/cmd?id=facelandmarks
# smart resize:           https://pixlab.io/#/cmd?id=smartresize
# merge:                  https://pixlab.io/#/cmd?id=merge
# Optionally: blur, grayscale, oilpaint, etc. for cool background effects.

$img = 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg';

$pix = new Pixlab('My_Pix_Key');
/* Grab the face landmarks first */
if( !$pix->get('facelandmarks',[
	'img' => $img
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}

$total = count($pix->json->faces); # Total detected faces
print($total." faces were detected\n");
$snap = [];
# Iterate all over the detected faces
foreach ($pix->json->faces as $face){
	$cord = $face->rectangle;
	# Show the face coordinates 
	print ("Coordinates...\n");
	print ("\n\twidth: " . $cord->width . ' height: ' . $cord->height . ' x: ' . $cord->left .' y: ' . $cord->top);
	
	# Show landmarks:
	print ("\nLandmarks...\n");
	
	$landmarks = $face->landmarks;
	
	print ("\n\tNose: X: "       . $landmarks->nose->x      . ", Y: ".$landmarks->nose->y);
	print ("\n\tBottom Lip: X: " . $landmarks->bottom_lip->x. ", Y: ".$landmarks->bottom_lip->y);
	print ("\n\tTop Lip: X: "    . $landmarks->top_lip->x   . ", Y: ".$landmarks->top_lip->y);
	print ("\n\tChin: X: "       . $landmarks->chin->x      . ", Y: ".$landmarks->chin->y);
	
	print ("\n\tBone Center: X: "     . $landmarks->bone->center->x     . ", Y: ".$landmarks->bone->center->y);
	print ("\n\tBone Outer Left: X: " . $landmarks->bone->outer_left->x . ", Y: ".$landmarks->bone->outer_left->y);
	print ("\n\tBone Outer Right: X: ". $landmarks->bone->outer_right->x. ", Y: ".$landmarks->bone->outer_right->y);
	
	print ("\n\tBone Center: X: " . $landmarks->bone->center->x . ", Y: ".$landmarks->bone->center->y);
	
	print ("\n\tEye Pupil Left: X: " . $landmarks->eye->pupil_left->x . ", Y: ".$landmarks->eye->pupil_left->y);
	print ("\n\tEye Pupil Right: X: " . $landmarks->eye->pupil_right->x . ", Y: ".$landmarks->eye->pupil_right->y);
	
	print ("\n\tEye Left Brown Inner: X: " . $landmarks->eye->left_brow_inner->x . ", Y: ".$landmarks->eye->left_brow_inner->y);
	print ("\n\tEye Right Brown Inner: X: " . $landmarks->eye->right_brow_inner->x . ", Y: ".$landmarks->eye->right_brow_inner->y);
	
	print ("\n\tEye Left Outer: X: " . $landmarks->eye->left_outer->x . ", Y: ".$landmarks->eye->left_outer->y);
	print ("\n\tEye Right Outer: X: " . $landmarks->eye->right_outer->x . ", Y: ".$landmarks->eye->right_outer->y); 
	
	# More landmarks on the docs..
	
	# Pick the last face in this loop for the sack of simplicity. Refer to the sample set for a complete example
	$snap = $face;
}
# Make a quick Snapchat filter on top of the last detected face
if ($total < 1){
    # No faces were detected
	die;
}
 
# The flower crown to be composited on top of the target face
$flower = 'http://pixlab.xyz/images/flower_crown.png';

# Resize the flower crown which is quite big right now to exactly the face width using smart resize.
print ("\nResizing the snap flower crown...\n");
if( !$pix->get('smartresize',[
	'img' => $flower,
	'width' => 20 + $snap->rectangle->width, # Face width
	'height' => 0 # Let Pixlab decide the best height for this picture
	]) ){
	echo $pix->get_error_message()."\n";
}else{
	$flower = $pix->json->link;
}
# Finally, Perform the composite operation
print ("Composite operation...\n");
if( !$pix->post('merge',[
	'src' => $img,
	'cord' => [
	array( /* Array for each landmarks */
		'img' => $flower,
		'x' => $snap->landmarks->bone->outer_left->x,
		'y' => $snap->landmarks->bone->outer_left->y /* Adjust for optimal effect */
	)
	]]) ){
	echo $pix->get_error_message();
}else{
	 # Optionally call blur, oilpaint, grayscale for more stuff..
	print ("Snap Filter Effect: ".$pix->json->link);
}
echo "\n";
?>
