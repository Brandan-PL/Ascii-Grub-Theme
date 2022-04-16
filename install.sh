#!/bin/bash

clear

python3 ./createTheme.py

echo "Copying the theme..."
sudo cp -r ./ascii_theme /boot/grub/themes/

echo "" | sudo tee -a /etc/default/grub > /dev/null
echo "# ASCII GRUB THEME" | sudo tee -a /etc/default/grub > /dev/null
echo "GRUB_THEME=/boot/grub/themes/ascii_theme/theme.txt" | sudo tee -a /etc/default/grub > /dev/null
echo "GRUB_GFXMODE=1920x1080,auto" | sudo tee -a /etc/default/grub > /dev/null

echo ""
echo "Updating GRUB..."
echo ""

sudo update-grub

echo ""
echo "Done. Enjoy ;)"
echo ""
