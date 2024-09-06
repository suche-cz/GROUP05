# matplot_line.py

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 40, 23, 29, 80]
y2 = [92, 2, 28, 27, 17]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='p', linestyle=':', color='r')
plt.plot(x, y2, marker='p', linestyle=':', color='b')
plt.title('Cena zlata')
plt.xlabel('Den')
plt.ylabel('Cena')
# plt.legend()
plt.grid(True)
plt.show()