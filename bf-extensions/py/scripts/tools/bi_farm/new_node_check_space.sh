#!/bin/bash

IP=$1

disk_free=`ssh $IP df /media/data/mango_farm_svn/ | tail -n 1 | sed -r 's/\s+/ /g' | cut -d \  -f  4`

# 5GB should be enough for farm
if [[ "$disk_free" -le 5242880 ]]; then
  echo "LOW"
else
  echo "OK"
fi
