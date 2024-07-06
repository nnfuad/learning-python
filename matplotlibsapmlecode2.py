import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.random.rand(10)
y5 = np.random.rand(10)

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axs[0, 0].plot(x, y1, label='sin(x)')
axs[0, 0].plot(x, y2, label='cos(x)')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Bar chart
bars = axs[0, 1].bar(range(len(y4)), y4, color='skyblue')
axs[0, 1].set_title('Bar Chart')
axs[0, 1].set_xlabel('Category')
axs[0, 1].set_ylabel('Value')

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

# Scatter plot
scatter = axs[1, 0].scatter(y4, y5, c='purple', marker='o')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')

# Histogram
axs[1, 1].hist(y4, bins=5, color='green', alpha=0.7)
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()
plt.suptitle('Complex Matplotlib Example', fontsize=16)
plt.subplots_adjust(top=0.92)

# Show plot
plt.show()