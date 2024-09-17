#!/bin/sh
#
#                  __           ____             ____ _____
#                 / _| ___ _ __|  _ \  _____   _|___ \___  |
#                | |_ / _ \ '__| | | |/ _ \ \ / / __) | / /
#                |  _|  __/ |  | |_| |  __/\ V / / __/ / /
#                |_|  \___|_|  |____/ \___| \_/ |_____/_/
#
#                  GitHub: https://github.com/ferDev27

# Composer
picom &

# Cursor speed
xset r rate 300 35 &

# Keyboard
setxkbmap -option "caps:escape_shifted_capslock" &

# Notifications
dunst &

# USB device helper
udiskie -A -t &

# Bluetooth systray applet
# blueman-applet &

# System trace
volumeicon &

