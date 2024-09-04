import matplotlib.pyplot as plt
import random

# Data
data = [random.randint(1, 100) for _ in range(50)]

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
