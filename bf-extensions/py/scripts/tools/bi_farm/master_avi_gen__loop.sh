#!/bin/bash
# simply call: 'master_avi_gen.py' in a loop
while true; do
	svn up ./mango_svn --accept theirs-full
	./master_avi_gen.py
	sleep 120
done