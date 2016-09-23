parted /dev/sdc mklabel gpt
parted /dev/sdc mkpart primary 0% 100%
sudo mkfs.ext4 /dev/sdc1
mkdir /home/negat/data
mount /dev/sdc1 /home/negat/data
