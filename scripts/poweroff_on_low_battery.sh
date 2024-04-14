#!/bin/sh

while [[ 1 ]]; do
	battery_level=$(cat /sys/class/power_supply/BAT0/capacity)

	if [[ battery_level -lt 5 ]]; then
		notify-send "Battery level critical." "Battery level reached critical level. Shutting down PC." -u critical

		for i in {5..1}; do
			notify-send "Shutdown" "Shutting down PC in $i." -u critical
			sleep 1
		done

		poweroff
	fi
	sleep 60
done
