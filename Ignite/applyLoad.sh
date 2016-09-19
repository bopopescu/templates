#!/bin/bash

ssh -p 50000 negat@51.141.13.25 'bash applyLoad.sh' &
ssh -p 50001 negat@51.141.13.25 'bash applyLoad.sh' &

#while [ 1==1 ]
#do
#    sleep .$(echo $RANDOM)
#    x=0
#    for i in `seq 1 10000`
#    do
#	x=$x+1
#    done
#done


