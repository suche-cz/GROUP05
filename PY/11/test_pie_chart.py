import matplotlib.pyplot as plt

# Data
sizes = [15, 30, 45, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D']
colors = ['gold', 'lightskyblue', 'lightcoral', 'lightgreen']

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.show()
