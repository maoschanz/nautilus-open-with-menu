#!/bin/bash

if (( $EUID == 0 )); then
	echo "Checking if adequate folders exist..."
	
	if [ ! -d "/usr/share/nautilus-python" ]; then
		mkdir /usr/share/nautilus-python
	fi
	if [ ! -d "/usr/share/nautilus-python/extensions" ]; then
		mkdir /usr/share/nautilus-python/extensions/
	fi
	
	echo "Installing plugin files in /usr/share/nautilus-python/extensions/"
	cp open-with-menu.py /usr/share/nautilus-python/extensions/open-with-menu.py

else
	echo "Checking if adequate folders exist..."
	
	if [ ! -d "$HOME/.local/share/nautilus-python" ]; then
		mkdir ~/.local/share/nautilus-python
	fi
	if [ ! -d "$HOME/.local/share/nautilus-python/extensions" ]; then
		mkdir ~/.local/share/nautilus-python/extensions/
	fi

	echo "Installing plugin files in ~/.local/share/nautilus-python/extensions"
	cp open-with-menu.py ~/.local/share/nautilus-python/extensions/open-with-menu.py

fi

exit 0
