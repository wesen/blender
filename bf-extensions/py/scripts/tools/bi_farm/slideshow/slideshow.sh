#!/bin/bash
while true
do
	mplayer -mf fps=0.01 -vo xv,x11 -fixed-vo -fs \
		mf:///shared/software/render_farm/slideshow/preview_big*.png

	sleep 1

done
