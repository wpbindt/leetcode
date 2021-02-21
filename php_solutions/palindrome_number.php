<?php

function isPalindromeByString($int) {
    $stringy_int = strval($int);
    return $stringy_int == strrev($stringy_int);
}

function isPalindrome($int) {
    if ($int < 0) {
        return false;
    }
    $digits = array();
    while ($int > 0) {
        array_push($digits, $int % 10);
        $int = floor($int / 10);
    }
    return $digits == array_reverse($digits);
} 


foreach ([1, 2, 121, 323, 444, 4224] as $num) {
    if (!isPalindrome($num)) {
        echo "nope";
    }
}

foreach ([12, -1, 19, 1212, 332] as $num) {
    if (isPalindrome($num)) {
        echo "nope";
    }
}

