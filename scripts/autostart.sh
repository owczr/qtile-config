#!/bin/sh

# start compositor
picom -b

# set monitor as primary
xrandr --output DP-1-1 --primary
# move laptop screen to the right
xrandr --output eDP-1 --right-of DP-1-1

# invert touchpad scrolling
xinput set-prop "AlpsPS/2 ALPS DualPoint TouchPad" 315 1
# touchpad tapping
xinput set-prop "AlpsPS/2 ALPS DualPoint TouchPad" 344 1

# turn on blue light filter
redshift -l 50.06143:19.93658 &

# start dunst for notifications
dunst &
