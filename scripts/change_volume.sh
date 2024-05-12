#!/bin/bash

method=$1

case "$method" in
"increase")
	amixer -q set Master 5%+
	;;
"decrease")
	amixer -q set Master 5%-
	;;
"mute")
	amixer -qD pulse set Master 1+ toggle
	;;
*)
	echo "ERROR: Wrong method selected."
	exit 1
	;;
esac

amixer sget Master | awk -F "[][]" '/Left:/ { print $2 }'
