#!/bin/bash

RANDOM=$$
ROWNUMBER=${1:-10}
for i in `seq $ROWNUMBER`
do 
echo $i "," $RANDOM >> input.csv
done