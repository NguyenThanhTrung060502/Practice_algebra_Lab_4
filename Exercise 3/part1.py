import matplotlib.pyplot as plt
import numpy as np 

# Set size for figure
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,7))
fig.suptitle('Gia tri rieng')

def Oxy(axes):
    plt.sca(axes)
	# Draw the coordinate system Oxy
    Ox = list(range(-2, 3, 1))
    Oy = list(range(-2, 3, 1))
    plt.xticks(Ox, color='black')
    plt.yticks(Oy, color='black')
    plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
    plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy	
	# This function is used to adjust so that the units of the Ox and Oy axes are equal 
    # plt.axis('equal')

def Draw_Eigenvalue(axes, vecto_1, vecto_2, color_1, color_2, vecto_name1, vecto_name2):
    plt.sca(axes)
    plt.quiver(0, 0, vecto_1[0], vecto_1[1], angles='xy', scale_units='xy', scale=1, color=f'{color_1}', label=f'{vecto_name1}', width=0.01, headwidth=2, headaxislength=3, headlength=4)
    plt.quiver(0, 0, vecto_2[0], vecto_2[1], angles='xy', scale_units='xy', scale=1, color=f'{color_2}', label=f'{vecto_name2}', width=0.01, headwidth=2, headaxislength=3, headlength=4)
    plt.grid(color = 'silver', linestyle = '--', linewidth = 0.5)
    plt.legend()

for i in range(2):
    for j in range(3):
        axes[i][j].set_xlabel('Re', color='black', fontsize=12)
        axes[i][j].set_ylabel('Im', color='black', fontsize=12)
        axes[i][j].xaxis.set_label_coords(1.05, 0.53)
        axes[i][j].yaxis.set_label_coords(0.5, 1.018)
        axes[i][j].yaxis.label.set_rotation(0)

eigenvalue1_1 = [-1, 0]
eigenvalue1_2 = [-1, 0]

eigenvalue2_1 = [-1/np.sqrt(2), 1/np.sqrt(2)]
eigenvalue2_2 = [-1/np.sqrt(2), -1/np.sqrt(2)]

eigenvalue3_1 = [0, 1]
eigenvalue3_2 = [0, -1]

eigenvalue4_1 = [1/np.sqrt(2), 1/np.sqrt(2)]
eigenvalue4_2 = [1/np.sqrt(2), -1/np.sqrt(2)]

eigenvalue5_1 = [1, 0]
eigenvalue5_2 = [1, 0]

eigenvalue6_1 = [-0.5, 0]
eigenvalue6_2 = [-0.5, 0]

for i in range(2):
    for j in range(3):
        Oxy(axes[i][j]) 

Draw_Eigenvalue(axes[0][0], eigenvalue1_1, eigenvalue1_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')
Draw_Eigenvalue(axes[0][1], eigenvalue2_1, eigenvalue2_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')
Draw_Eigenvalue(axes[0][2], eigenvalue3_1, eigenvalue3_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')

Draw_Eigenvalue(axes[1][0], eigenvalue4_1, eigenvalue4_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')
Draw_Eigenvalue(axes[1][1], eigenvalue5_1, eigenvalue5_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')
Draw_Eigenvalue(axes[1][2], eigenvalue6_1, eigenvalue6_2, 'green', 'darkviolet', 'Eigenvalue 1', 'Eigenvalue 2')


# Show graph
plt.show()