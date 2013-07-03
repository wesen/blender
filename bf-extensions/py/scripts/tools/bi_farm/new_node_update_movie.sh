#!/bin/bash
FARM_DIR=/shared/software/render_farm
PATH=$PATH:$FARM_DIR
export IP=`ip.sh`
BUSY=$FARM_DIR/logs/$IP.busy
SVN_IP="192.168.3.14"

DIR="/media/data/mango_farm_svn"
REV=$1

echo "Updating SVN Production Files to "$REV > $BUSY

if [ -d $DIR ]; then
	cd $DIR
	svn cleanup --config-dir=$FARM_DIR/svn_config
    # TEMP DISABLE, for physics bake
	svn revert --config-dir=$FARM_DIR/svn_config -R .
	
	
	# HACK: XXX, run a different update that removes corrupt dirs
	### $FARM_DIR/new_node_command.sh svn up --config-dir=$FARM_DIR/svn_config --force -r$REV
	$FARM_DIR/new_node_command.sh /shared/software/python/bin/python3 $FARM_DIR/svn_force_update.py /usr/bin/svn up --config-dir=$FARM_DIR/svn_config --force -r$REV
	
else
	# $FARM_DIR/new_node_command.sh svn co --config-dir=$FARM_DIR/svn_config --force -r$REV svn://$SVN_IP/mango/pro $DIR/pro
    #$FARM_DIR/new_node_command.sh svn co --config-dir=$FARM_DIR/svn_config --force -r$REV file:///svnroot/mango/pro $DIR/pro
    $FARM_DIR/new_node_command.sh svn co --config-dir=$FARM_DIR/svn_config --force -r$REV svn://$SVN_IP/mango $DIR
fi

rm $BUSY
