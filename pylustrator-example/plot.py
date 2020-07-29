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


#% start: automatic generated code from pylustrator
plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
import matplotlib as mpl
plt.figure(1).set_size_inches(11.160000/2.54, 10.160000/2.54, forward=True)
plt.figure(1).axes[0].legend(handlelength=1.5999999999999999, ncol=2, fontsize=16.0, title_fontsize=16.0)
plt.figure(1).axes[0].set_position([0.162422, 0.656584, 0.775000, 0.226471])
plt.figure(1).axes[0].set_xlim(-0.6283185307179586, 13.194689145077131)
plt.figure(1).axes[0].set_xticklabels(["0", "2", "4", "6", "8", "10"])
plt.figure(1).axes[0].set_xticks([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
plt.figure(1).axes[0].xaxis.labelpad = -5.000000
plt.figure(1).axes[0].get_legend()._set_loc((0.134094, 1.008221))
plt.figure(1).axes[0].get_legend()._set_loc((0.174333, 1.028337))
plt.figure(1).axes[0].get_xaxis().get_label().set_text("x")
plt.figure(1).axes[0].get_yaxis().get_label().set_text("y")
plt.figure(1).axes[1].set_position([0.162422, 0.194977, 0.334252, 0.226471])
plt.figure(1).axes[1].xaxis.labelpad = -3.692585
plt.figure(1).axes[1].get_xaxis().get_label().set_text("x")
plt.figure(1).axes[1].get_yaxis().get_label().set_text("y")
plt.figure(1).axes[2].set_position([0.603170, 0.194977, 0.334252, 0.226471])
plt.figure(1).axes[2].get_xaxis().get_label().set_text("x")
plt.figure(1).text(0.5, 0.5, 'New Text', transform=plt.figure(1).transFigure)  # id=plt.figure(1).texts[0].new
plt.figure(1).texts[0].set_position([0.046778, 0.905467])
plt.figure(1).texts[0].set_text("a)")
plt.figure(1).text(0.5, 0.5, 'New Text', transform=plt.figure(1).transFigure)  # id=plt.figure(1).texts[1].new
plt.figure(1).texts[1].set_position([0.046778, 0.443052])
plt.figure(1).texts[1].set_text("b)")
plt.figure(1).text(0.5, 0.5, 'New Text', transform=plt.figure(1).transFigure)  # id=plt.figure(1).texts[2].new
plt.figure(1).texts[2].set_position([0.537422, 0.443052])
plt.figure(1).texts[2].set_text("c)")
#% end: automatic generated code from pylustrator
plt.show()