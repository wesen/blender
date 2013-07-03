#!/bin/bash

PATH=$PATH:$FARM_DIR
export IP=`ip.sh`
BUSY=$FARM_DIR/logs/$IP.busy
BINARY="blender_farm"

echo "Cleaning..." > $BUSY

# do this first to signal that new jobs shouldnt spawn once blender is killed
rm $BUSY

# ignore error incase 'new_node_command.sh' isn't running
pkill -P $(pgrep -f new_node_command.sh) 2> /dev/null
killall -9 $BINARY

rm -rf /tmp/mango_farm*

