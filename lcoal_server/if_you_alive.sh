#!/bin/bash

export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

echo $(arp-scan -I wan -l) > /root/iptable.log && status=$(cat /root/iptable.log|grep 00:0e:c6:cc:d1:0a)

time3=$(date "+%Y-%m-%d %H:%M:%S")

if [ "$status" != "" ];then
# boss here
	cp /root/1.png /root/Image.png
	echo $time3 "1"
else
# not here
	cp /root/0.png /root/Image.png
	echo $time3 "0"
fi

cd /root
gnuplot plot.sh
cp /root/2.png /root/Image[1].png
