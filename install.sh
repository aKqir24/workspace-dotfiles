#!/bin/bash

packages=( 
	i3
	mpv
	btop
	gimp
	rofi
	kitty
	bluez
	neovim
	gparted
	polybar
	shotcut
	pcmanfm
	viewnior
	pipewire
	siji-ttf
	bluez-libs
	winetricks
	obs-studio
	bluez-utils
	imagemagick
	pulsemixer	
	wireplumber
	vscodium-bin
	pipewire-jack
	wine-stagging
	xgifwallpaper
	rofi-emoji-git
	pipewire-pulse
	zen-browser-bin	
    gimp-plugin-gmic	
	libreoffice-fresh	
	picom-pijulius-next-git 
)

for pkg in ${packages[@]}; do
	yay -S --noconfirm ${pkg}
done
