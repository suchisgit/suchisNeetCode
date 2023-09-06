<?php

function isPerfectNumber(int $input){
    $divisorSum = 0;
    $sumsString = "";
    if($input == 0){
        $input =1;
    }
    for($i=1;$i<$input;$i++){
        if ($input%$i ==0 ){
            $divisorSum += $i;
            $sumsString .= $i . "+";
            // echo $sumsString;
        }
    }
    if ($divisorSum == $input){
        return "Yes, this is a perfect number. Proof: " . rtrim($sumsString, "+") . " = " . $divisorSum . "\n";
    }else{
        return "No, this is not a perfect number. Proof: " . rtrim($sumsString, "+") . " != " . $divisorSum . "\n";
    }
}

function tester_function(){
    $testcases = [['input' => 6, 'expected' => true],['input' => 3, 'expected' => true]];
    // $testcases = [['input' => 6, 'expected' => true],['input' => 0, 'expected' => false]];
    foreach ($testcases as $testcase){
        $input = $testcase['input'];
        $expectedResult = $testcase['expected'];
    $res = isPerfectNumber($input);
    if ( (stripos($res,"Yes")!== false) && ($expectedResult == true)){
        echo "yes, test passed\n";
    }else if( (stripos($res,"No")!== false) && ($expectedResult == false)){
        echo "yes, test passed\n";
    }
    else{
        echo "no, test failed\n";
    }
    }
}
$result = isPerfectNumber(6);
echo $result;
tester_function()

?>
