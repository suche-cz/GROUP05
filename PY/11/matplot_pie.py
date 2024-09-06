# matplot_pie.py

import matplotlib.pyplot as plt

hodnoty = [40, 60, 10, 50]
popisky = ['Zletilý', 'Nezletilý', 'Y', 'X']
# barvy = ['red', 'blue'] #006699

plt.figure(figsize=(8, 8))
plt.pie(hodnoty, labels=popisky, startangle=90)

plt.show()



