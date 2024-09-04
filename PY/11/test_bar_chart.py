import matplotlib.pyplot as plt

# Data
data = {
    'Apples': 10,
    'Bananas': 15,
    'Cherries': 7,
    'Dates': 5
}

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(data.keys(), data.values(), color='purple')
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Quantity Sold")
plt.show()
