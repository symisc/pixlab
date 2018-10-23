<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Given a government issued passport document, extract the user face and parse all MRZ fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://pixlab.io/dashboard
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/cmd?id=docscan for additional information.

/* Passport prototype: Of course, replace with a real government issued passport if you 
 * want to deal with a real world situation.
 */
$passport = 'https://i.stack.imgur.com/oJY2K.png';

# Your PixLab key
$key = 'My_PixLab_Key';

/* Process */
$pix = new Pixlab($key);
if( !$pix->get('docscan',[
	'img' => $passport,  /* Passport scanned image */ 
	'type' => 'passport' /* Type pf document we are going to scan */ 
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
/* Output the scan result */
echo "User Cropped Face: " . $pix->json->face_url . "\n";
echo "MRZ Cropped Image: " . $pix->json->mrz_img_url . "\n";
echo "Raw MRZ Text: " . $pix->json->mrz_raw_text . "\n";
echo "MRZ Fields:\n";
/* Display all parsed MRZ fields */
echo "\tIssuing Country: " . $pix->json->fields->issuingCountry . "\n";
echo "\tFull Name: "       . $pix->json->fields->fullName . "\n";
echo "\tDocument Number: " . $pix->json->fields->documentNumber  . "\n";
echo "\tCheck Digit: "   . $pix->json->fields->checkDigit . "\n";
echo "\tNationality: "   . $pix->json->fields->nationality . "\n";
echo "\tDate Of Birth: " . $pix->json->fields->dateOfBirth . "\n";
echo "\tSex: "           . $pix->json->fields->sex . "\n";
echo "\tDate Of Expiry: "    . $pix->json->fields->dateOfExpiry . "\n";
echo "\tPersonal Number: "   . $pix->json->fields->personalNumber . "\n";
echo "\tFinal Check Digit: " . $pix->json->fields->finalcheckDigit . "\n";
?>
