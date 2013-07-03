#!/bin/bash
# wrapper so we can do a simple killall to stop any a command 
umask 0000
echo $@
$@

