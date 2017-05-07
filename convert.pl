#!/usr/bin/perl

print "Enter a value (e.g. 30 deg, 0.5 rad...): ";
$input = <STDIN>;
chomp($input);

if ($input =~ m/((?:\d*\.)?(?:\d+))[\s]+(deg|rad)/i) {
  if ($2 eq "deg") {
    $result = (3.14 * $1) / 180;
    printf "$input in radians = %.02f\n", $result;
  } else {
    $result = (180 * $1) / 3.14;
    printf "$input in degrees = %.02f\n", $result;
  }
} else {
  print "Could not recognize \"$input\"\n";
}
