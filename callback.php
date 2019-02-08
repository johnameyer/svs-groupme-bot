<?php
$data = json_decode(file_get_contents('php://input'), true);
if(!strcasecmp($data['text'], '/pay respects')){
	echo `./pay_respects.py`;
}
$text = split(' ', $data['text']);
if(!strcasecmp($text[0], '/roast')){
	echo `./roast.py $text[1]`;
}
