import matplotlib.pyplot as plt

# Data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
data = [10, 15, 7, 5]

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(fruits, data, color='purple')
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Quantity Sold")
plt.show()
