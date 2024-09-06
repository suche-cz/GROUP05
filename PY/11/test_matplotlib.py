# test_matplotlib.py

# python -m pip install matplotlib
# python -m pip uninstall matplotlib
# 'C:/Python/Python311/Lib/site-packages/matplotlib/__init__.py'
import matplotlib
import test_script # site-packages
import test_script2 # same folder

# pokračujeme v 20:06

import os
import sys
print(sys.path)
print(os.getcwd())

print(test_script.JMENO)
print(test_script.vypocitej(1, 2, 3))

