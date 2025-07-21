
read expression

a=`echo $expression | bc -l`
printf "%.3f" $a