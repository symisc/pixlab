<?php
/*
 * Usage sample of the ID card scanner from PixLab. In this sample, we shall scan
 * ID Card from Malaysia (MyKAD); therefore we will extract the user's face, date of birth,
 * full name, address, and religion if available.
 */ 
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
# Given a government issued ID card from Malaysia, UAE, India, US Driver, Singapore, etc., extract the user face and parse all fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://pixlab.io/dashboard
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/cmd?id=docscan for additional information.

$idcard_link = 'https://buletinonline.net/v7/wp-content/uploads/2016/06/Mykad-penghuni-puan-Noraini-2.jpg'; /* ID card prototype: Of course, replace with a real government issued id. */
$key = 'PIXLAB_API_KEY'; # Your PixLab API key that you can fetch from https://pixlab.io/dsahboard
/* Process */
$pix = new Pixlab($key);
if( !$pix->get('docscan',[
	'img' => $idcard_link, # ID Card Scanned Image
	'type' => 'idcard', # Type of document we are going to scan 
	'country' => 'my' # Malysia country code
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
/* Output the scan result */
echo "User Cropped Face: " . $pix->json->face_url . "\n";
#echo "Raw Text: " . $pix->json->full_text . "\n";
echo "Fields:\n";
# At this stage, the face should be extracted and the array populated with the appropriate information.
if( isset($pix->json->country) )  echo  "Country: ".$pix->json->fields->country . "\n";
if( isset($pix->json->fields->id) )       echo  "ID: ".$pix->json->fields->id . "\n";
if( isset($pix->json->fields->name) )     echo  "Name: ".$pix->json->fields->name . "\n";
if( isset($pix->json->fields->address) )  echo  "Address: ".$pix->json->fields->address . "\n";
if( isset($pix->json->fields->religion) ) echo  "Religion: ".$pix->json->fields->religion . "\n";
if( isset($pix->json->fields->sex) )      echo  "Sex: ".$pix->json->fields->sex . "\n";
if( isset($pix->json->fields->race) )     echo  "Race: ".$pix->json->fields->race . "\n";
if( isset($pix->json->fields->birth) )    echo  "Date of birth: ".$pix->json->fields->birth . "\n";
if( isset($pix->json->fields->birth_country) ) echo  "Country of birth: ".$pix->json->fields->birth_country . "\n";
if( isset($pix->json->fields->nationality) )   echo  "Nationality: ".$pix->json->nationality . "\n";
?>
