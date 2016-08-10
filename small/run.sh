#!/bin/bash

locArray=(eastasia southeastasia northeurope westeurope japaneast brazilsouth australiaeast australiasoutheast canadacentral canadaeast)

rm -f tmp/*


for i in $(seq 0 9)
do
    
    curRand=$RANDOM
    bash subrun.sh $1 $curRand ${locArray[$i]} &> tmp/out$curRand.txt &

done
