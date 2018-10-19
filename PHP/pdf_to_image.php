<?php
/*
 * PixLab PHP Client which is just a single class PHP file without any dependency that you can get from Github
 * https://github.com/symisc/pixlab-php 
 */
require_once "pixlab.php";

# Convert a PDF document to a high resolution JPEG/PNG image via /pdftoimg. 
# https://pixlab.io/cmd?id=pdftoimg for additional information.

# Target PDF to convert
$pdf  = 'https://www.getharvest.com/downloads/Invoice_Template.pdf';

# Invoke the endpoint
$pix = new Pixlab('My_Pix_Key');
if( !$pix->get('pdftoimg',[
	'src' => $pdf,
	'export' => 'png'
]) ){
	echo $pix->get_error_message()."\n";
	die;
}
echo "Link to the image output (Converted PDF page): ".$pix->json->link."\n";
?>
