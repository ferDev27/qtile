#!/bin/sh
#
#                  __           ____             ____ _____
#                 / _| ___ _ __|  _ \  _____   _|___ \___  |
#                | |_ / _ \ '__| | | |/ _ \ \ / / __) | / /
#                |  _|  __/ |  | |_| |  __/\ V / / __/ / /
#                |_|  \___|_|  |____/ \___| \_/ |_____/_/
#
#                  GitHub: https://github.com/ferDev27

# Monitor settings
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | cut -d' ' -f1`

if [ "$hdmi" = "HDMI-1" ]; then
  xrandr --output HDMI-1 --primary --auto --output eDP-1 --off & # Only use one external monitor
else
  xrandr --output eDP-1 --primary --auto --pos 0x0 --rotate normal &
fi

# ENV
QT_STYLE_OVERRIDE=kvantum &

# Composer
picom &

# Notification
dunst &

# Cursor speed
xset r rate 300 35 &

# Keyboard
setxkbmap -option "caps:escape_shifted_capslock" &

# System trace
volumeicon &

