#!/usr/bin/env bash

# Resolution Display
xrandr --newmode "1152x864_60.00"   81.75  1152 1216 1336 1520  864 867 871 897 -hsync +vsync ;
xrandr --addmode VGA1 "1152x864_60.00" ; xrandr --output VGA1 --mode "1152x864_60.00" &

# Start / Restart Program
killall -q polybar ; pkill xgifwallpaper ; pkill autotiling ; pkill dunst ; pkill picom ;
xgifwallpaper -s FILL --scale-filter PIXEL -d 16 /home/Akqir/Pictures/Wallpaper/Gif/nautr_girl.gif & 
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log & polybar bar1 2>&1 | tee -a /tmp/polybar1.log & 
disown & picom & autotiling & dunst &
