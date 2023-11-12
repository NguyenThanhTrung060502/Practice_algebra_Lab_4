import numpy as np 
import matplotlib.pyplot as plt 

# fig, axes = plt.subplots(nrows=3, ncols=4)
fig, axes = plt.subplots(nrows=3, ncols=1)

# Set the ticks and ticklabels for all axes
plt.setp(axes, xticks=[1], xticklabels=['t'], yticks=[1], yticklabels=['x(t)'])


# Use the pyplot interface to change just one subplot...
plt.sca(axes[1])
plt.xticks(range(1), ['t'], color='red')


fig.tight_layout()
plt.show()