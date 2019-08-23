#!/bin/bash

echo "Checking if adequate folders exist…"
if (( $EUID == 0 )); then
	dir_pyt_ext="/usr/share/nautilus-python/extensions"
else
	dir_pyt_ext="$HOME/.local/share/nautilus-python/extensions"
fi

mkdir -p "${dir_pyt_ext}"
echo "Installing plugin files in $dir_pyt_ext"
cp open-with-menu.py $dir_pyt_ext/open-with-menu.py

echo "Done."
exit 0

