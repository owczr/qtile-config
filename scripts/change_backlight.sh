#!/bin/bash

MINIMUM=1
MAXIMUM=937
STEP=93

brightness=$(cat /sys/class/backlight/intel_backlight/brightness)

case "$1" in
"increase")
	brightness=$((brightness + $STEP))
	;;
"decrease")
	brightness=$((brightness - $STEP))
	;;
*)
	exit 1
	;;
esac

if [[ $brightness -gt $MAXIMUM ]]; then
	brightness=$MAXIMUM
fi
if [[ $brightness -lt $MINIMUM ]]; then
	brightness=$MINIMUM
fi

echo "$brightness" >/sys/class/backlight/intel_backlight/brightness

echo "($brightness  / $MAXIMUM)" | bc -l
