# 18/12/2021
# guilherme Silva Toledo
# code to read my twitter timeline and generate me some new banner every few seconds

import os

os.system('sudo xrandr --newmode "1504x500_60.00" 58.75  1504 1552 1696 1888  500 503 513 521 -hsync +vsync')


os.system('sudo xrandr --addmode Virtual1 1504x500_60.00')

os.system('xrandr --output Virtual1 --mode "1504x500_60.00"')
