#!/bin/bash
export PATH="$HOME/bin:$PATH"
export XDG_CURRENT_DESKTOP=bspwm
export XDG_SESSION_TYPE=x11

# Start WM
exec bspwm
exec sxhkd
exec pipewire 
exec pipewire-pulse 
exec wireplumber
