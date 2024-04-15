#!/bin/bash

kill_processes() {
	# kills process other than itself
	for pid in $(pgrep -u $USER); do
		if [[ "$pid" != "$$" ]]; then
			kill -SIGTERM "$pid"
		fi
	done
}

while true; do
	battery_level=$(cat /sys/class/power_supply/BAT0/capacity)

	if [[ "$battery_level" -lt 5 ]]; then
		notify-send "Battery level critical." "Battery level reached critical level. Shutting down PC." -u critical

		for ((i = 5; i > 0; i--)); do
			notify-send "Shutdown" "Shutting down PC in $i." -u critical
			sleep 1
		done

		kill_processes

		sleep 5

		poweroff
	fi
	sleep 60
done
