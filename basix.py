from basparse import parser
from basinterp import Interpreter

data = """
<?php //php 7.2.24
    $num1=10;
    $num2=20;
    IF ($num1>$num2) {
      $bignum = $num1;
      PRINT "Big Number is " . $bignum;
      }
    ELSE {
      $bignum = $num2;
      PRINT "Big Number is " . $bignum;
    }
?>

"""

data1 = """
    <?php //php 7.2.24
    PRINT "List of Odd Number 1-100:\n";
    PRINT "\n";
    $num=1;
    WHILE ($num<=100) {
        IF (($num % 2)!=0) {
            $oddnum=$num;
            PRINT "".$num." "; }
        $num=$num+1;
    }
?>

"""

data2 = """
    <?php
$num1 = 10;  
$num2 = 20;
$num3 = 30;
$sum = $num1 + $num2 + $num3;
$avg = $sum/3;
PRINT "Num1 is " . $num1 ."\n";
PRINT "Num2 is " . $num2 ."\n";
PRINT "Num3 is " . $num3 ."\n";
PRINT "Sum 3 numbers is " . $sum ."\n";
PRINT "Average is " . $avg;
?> 

"""

data3 = """
    <?php //php 7.2.24

    PRINT "Hello, world! \n";
    ECHO "Welcome ";
    
?>

"""

ast = parser.parse(data3)
interpreter = Interpreter()
interpreter.run(ast)
