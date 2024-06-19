<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Scan over 11K ID Documents from over 197 countries using the PixLab DOCSCAN API Endpoint
# documented at: https://ekyc.pixlab.io/docscan
#
# In this example, given a Passport document, extract the passport holder face and convert/parse all Machine Readable Zone
# to textual content ready to be consumed by your application.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://console.pixlab.io
# so that any extracted face or MRZ crop is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# Refer to the official documentation at: https://ekyc.pixlab.io/docscan for the API reference guide and more code samples.

# Passport prototype: Of course, replace with a real government issued passport if you 
# want to deal with a real world situation.
$passport = 'https://i.stack.imgur.com/oJY2K.png';

# Your PixLab API Key - Get yours from https://console.pixlab.io
$key = 'PIXLAB_API_KEY';

/* Process */
$pix = new Pixlab($key);
if( !$pix->get('docscan',[
	'img' => $passport,  # Passport input image
	'type' => 'passport' # Type of document we are going to scan
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
