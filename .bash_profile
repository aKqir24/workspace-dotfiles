#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ -d "$HOME/adb-fastboot/platform-tools" ] ; then
 export PATH="$HOME/adb-fastboot/platform-tools:$PATH"
fi

if [ -z "$DISPLAY"] && [ "$(tty)" = "/dev/tty1" ]; then
	exec startx
fi

