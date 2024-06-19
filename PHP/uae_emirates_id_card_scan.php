<?php
/*
 * Usage sample of the UAE ID card scanner API endpoint from PixLab - https://pixlab.io/cmd?id=docscan.
 */ 
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
# Scan over 11K ID Documents from over 197 countries using the PixLab DOCSCAN API Endpoint
# documented at: https://ekyc.pixlab.io/docscan
#
# In this example, given a government issued ID card from the UAE (emirates). Extract the holder's face and display all scanned fields.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://console.pixlab.io
# so that any extracted face or MRZ crop is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.

$idcard_link = 'https://pixlab.xyz/images/pixlab-uae-id.jpg'; # ID card prototype: Of course, replace with a real government issued id

$key = 'PIXLAB_API_KEY'; # Your PixLab API key that you can fetch from https://console.pixlab.io
# Start the scan Process
$pix = new Pixlab($key);
if( !$pix->get('docscan',[
	'img' => $idcard_link, # UAE ID Card Input image (https://pixlab.xyz/images/pixlab-uae-id.jpg). POST method for direct upload is also supported
	'type' => 'idcard', # Type of document we are going to scan 
	'country' => 'uae' # from the Emirates, we support also Malaysia/India/Singapore/US and Passports, 
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
# Output the scan result
echo "ID Card Holder's Face: " . $pix->json->face_url . "\n";
echo "Scanned Card Fields:\n";
# At this stage, the face should be extracted and the JSON object populated with the appropriate information.
if( isset($pix->json->fields->issuingCountry) )  echo  "Issuing Country: ".$pix->json->fields->issuingCountry . "\n";
if( isset($pix->json->fields->documentNumber) )  echo  "Document Number : ".$pix->json->fields->documentNumber . "\n";
if( isset($pix->json->fields->fullName) )     echo  "Holder Full Name: ".$pix->json->fields->fullName . "\n";
if( isset($pix->json->fields->nationality) )  echo  "Holder's Nationality: ".$pix->json->fields->nationality . "\n";
