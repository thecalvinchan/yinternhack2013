<?php
/**
 * create image from base64 encoding
 *
 */

define(EXTENSION,'.png');
$prefix = 'temp_';
$filename = '';

if(isset($_POST['base64'])) {
	$data = $_POST['base64']; 
} else {

// default data
$data = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAASCAMAAAB/2U7WAAAABl'
       . 'BMVEUAAAD///+l2Z/dAAAASUlEQVR4XqWQUQoAIAxC2/0vXZDr'
       . 'EX4IJTRkb7lobNUStXsB0jIXIAMSsQnWlsV+wULF4Avk9fLq2r'
       . '8a5HSE35Q3eO2XP1A1wQkZSgETvDtKdQAAAABJRU5ErkJggg==';
}


$data = base64_decode($data);


$im = imagecreatefromstring($data);
if ($im !== false) {
    $count = 0;
    $filename = $prefix  . $count . EXTENSION;
     while (file_exists($filename)) {
	    $count++;
	    $filename = $prefix  . $count . EXTENSION;
    }
    $status = imagepng($im, $filename);
    $output = shell_exec("python imageproc.py " . $filename); 
    unlink($filename);
    header('Content-Type: application/json');
    echo $output;
}
else {
    echo 'An error occurred.';
}
