while [ 1==1 ]
do
    bash applyLoadPagerDuty.sh
    sleep 300
    bash removeLoadPagerDuty.sh
    sleep 300
done
