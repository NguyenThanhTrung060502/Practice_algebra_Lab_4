import matplotlib.pyplot as plt
import numpy as np 

def Oxy():
	# Draw the coordinate system Oxy
	Ox = list(range(-3, 4, 1))
	Oy = list(range(-3, 4, 1))
	plt.xticks(Ox, color='white')
	plt.yticks(Oy, color='white')
	plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
	plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy	
	# This function is used to adjust so that the units of the Ox and Oy axes are equal 
	plt.axis('equal')


def Draw_Eigenvector(vecto, color, vecto_name):
    ax.quiver(0, 0, vecto[0], vecto[1], angles='xy', scale_units='xy', scale=1, color=f'{color}', label=f'{vecto_name}', width=0.004, headwidth=2, headaxislength=3, headlength=4)
    
    # Customize the limits of the x and y axis
    ax.set_xlim([0, max(vecto[0], 1)])
    ax.set_ylim([0, max(vecto[0], 1)])
    
    # Name the x and y axesa
    ax.set_xlabel('X')
    ax.set_ylabel('Y')


# Set size and set background for figure
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('black')

eigenvector_1 = [1, 0]
eigenvector_2 = [1, 1]

plt.grid(color = 'silver', linestyle = '--', linewidth = 0.5)

Draw_Eigenvector(eigenvector_1, 'darkviolet', 'Eigenvector 1')
Draw_Eigenvector(eigenvector_2, 'mediumaquamarine', 'Eigenvector 2')
Oxy()


plt.legend()

plt.show()