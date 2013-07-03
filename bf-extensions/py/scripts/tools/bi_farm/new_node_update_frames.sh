#!/bin/bash
PATH=$PATH:$FARM_DIR
export IP=`ip.sh`
BUSY=$FARM_DIR/logs/$IP.busy

touch $BUSY

mkdir /tmp/mango_farm

if [ ! -f $BUSY ] ; then
	echo "busy file removed, exiting early"
	exit 0
fi

BLEND=$1
PROCESSOR=$2
OUTPUT_BLEND=$3
QUALITY=$4

# skip 4 args above
shift
shift
shift
shift

# get info on the file we're rendering
echo "Rendering "${BLEND/\/media\/data\/mango_farm_svn\//}" "$* > $BUSY

for FRAME in $*
do
    # -a doesnt work. TODO, find out why, render with operator until then.
    $FARM_DIR/new_node_command.sh nice -n 19 $FARM_DIR/blender_farm.sh --background -noaudio $BLEND --python $FARM_DIR/new_blender_setup.py -- $PROCESSOR $OUTPUT_BLEND $FRAME $QUALITY &
    # no background for testing...
    # $FARM_DIR/new_node_command.sh nice -n 19 $FARM_DIR/blender_farm.sh -noaudio $BLEND --python $FARM_DIR/new_blender_setup.py -- $OUTPUT_BLEND $FRAME $QUALITY &
done

wait

rm $BUSY
