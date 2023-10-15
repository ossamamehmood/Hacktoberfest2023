<?php

function fibonacci($n) {
    if ($n <= 0) {
        return 0;
    } elseif ($n == 1) {
        return 1;
    } else {
        return fibonacci($n - 1) + fibonacci($n - 2);
    }
}

$n = 10; // Change this value to the number of Fibonacci sequence terms you want to calculate
for ($i = 0; $i < $n; $i++) {
    echo fibonacci($i) . " ";
}