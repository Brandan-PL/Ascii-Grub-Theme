#!/bin/bash

clear

python3 ./createTheme.py

echo "Copying the theme..."

sudo cp -r ./ascii_theme /boot/grub/themes/

sudo echo "GRUB_THEME=/boot/grub/themes/ascii_theme/theme.txt" >> /etc/default/grub
sudo echo "GRUB_GFXMODE=1920x1080,auto" >> /etc/default/grub


echo "Updating GRUB..."

update-grub

echo "Done. Enjoy ;)"
