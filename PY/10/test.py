import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create horizontal bar chart
plt.barh(categories, values)

# Add title and labels
plt.title("Simple Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")

# Show plot
plt.show()