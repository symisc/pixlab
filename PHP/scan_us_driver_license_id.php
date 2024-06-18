<?php
/*
 * Usage sample of the US Driver's License card scanner, API endpoint from PixLab - https://pixlab.io/cmd?id=docscan.
 */ 
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";
# Scan over 11K ID Documents from over 197 countries using the PixLab DOCSCAN API Endpoint
# documented at: https://ekyc.pixlab.io/docscan
#
# In this example, given a submitted/uploaded, US Driver License image document from any of the 50 US state
# crop the license holder face, and extract all document fields (see below) ready to be consumed by your application.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://console.pixlab.io
# so that any extracted face or MRZ crop is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# Refer to the official documentation at: https://ekyc.pixlab.io/docscan for the API reference guide and more code samples.

$us_driver_license_sample_link = 'https://www.aulicense.com/wp-content/uploads/2020/12/USA-DRIVERS-LICENSE.jpg';
$key = 'PIXLAB_API_KEY'; # Your PixLab API key that you can fetch from https://console.pixlab.io

# Start the scan Process
$pix = new Pixlab($key);
if( !$pix->get('docscan',[
	'img' => $us_driver_license_sample_link, # US Driver license input image
	'type' => 'usdl' # Type of document we are a going to scan, hence US driver license
	]) ){
	echo $pix->get_error_message()."\n";
	die;
}
# Consume the scan output
echo "License Holder Crooped Face: " . $pix->json->face_url . "\n";
echo "Extracted Fields:\n";
# At this stage, all license images fields should be extracted and the JSON object populated with the appropriate information.
echo  "Issuing Country: ".$pix->json->fields->country . "\n";
echo  "Issuing State: ".$pix->json->fields->issuingState . "\n";
echo  "Issuing State Code: ".$pix->json->fields->issuingStateCode . "\n";
echo  "Holder Full Name: ".$pix->json->fields->fullName . "\n";
echo  "License Number: ".$pix->json->fields->documentNumber . "\n";
echo  "Holder's Address: ".$pix->json->fields->address . "\n";
echo  "Date Of Birth: ".$pix->json->fields->dateOfBirth . "\n";
echo  "issuing Date: ".$pix->json->fields->issuingDate . "\n";
echo  "Date Of Expiry: ".$pix->json->fields->dateOfExpiry . "\n";
echo  "Gender: ".$pix->json->fields->sex . "\n";
