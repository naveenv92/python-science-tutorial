# Import packages
import matplotlib.pyplot as plt
import numpy as np
import pylustrator

# Use scientific plot style
plt.style.use('scientific')

# Create dummy data
x = np.linspace(0, 4*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# Start pylustrator
pylustrator.start()

# Create panelled figure
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

# Plot data
# Subplot 1
ax1.plot(x, y1, label='y1')
ax1.plot(x, y2, label='y2')
ax1.legend()

# Subplot 2
ax2.plot(x, y1)

# Subplot 3
ax3.plot(x, y2)

plt.show()