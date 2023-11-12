import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(17, 11))

# Set labels for each graph
for i in range(2):
    for j in range(3):
        axes[i][j].set_xlabel('k', color='black', fontsize=12)
        axes[i][j].set_ylabel('x(k)', color='black', fontsize=12)
        axes[i][j].xaxis.set_label_coords(1.02, 0.52)
        axes[i][j].yaxis.set_label_coords(0.5, 1.016)
        axes[i][j].yaxis.label.set_rotation(0)
            
def Oxy(axes):
    plt.sca(axes)
    # Draw the coordinate system Oxy
    Ox = np.arange(-12,13,2)
    Oy = np.arange(-12,13,2)
    # Set the color for the values of the Ox axis and Oy axis
    plt.grid(linestyle="--", color="silver", linewidth=0.5)
    plt.xticks(Ox, color='black')
    plt.yticks(Oy, color='black')
    plt.xlim(-12, 12)
    plt.ylim(-12, 12)
    plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # axis Ox
    plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # axis Oy

def Draw_graphs(axes, k, x1, x2, title, color_1, color_2):
    plt.sca(axes)
    plt.title(f'{title}', color='red', loc='left', fontname='Times New Roman', fontsize=12.5)
    plt.plot(k, x1, color=f'{color_1}' , linewidth=1.25, label=r'$x_{1}(k)$') 
    plt.plot(k, x2, color=f'{color_2}' , linewidth=1.25, label=r'$x_{2}(k)$')
    plt.legend()   

h = np.arange(0, 20, 0.001)
  
k = np.arange(0, 20, 1)
# Part 1
x1_1 = 2*((-1)**k) - ((-1)**k)*k
x2_1 = (-1)**k
# # Part 2
x1_2 = np.cos(h*(np.pi/4)) - 2*np.sin(h*(np.pi/4))
x2_2 = 2*np.cos(h*(np.pi/4)) + np.sin(h*(np.pi/4))
# # Part 3
x1_3 = np.cos(h*(np.pi/2)) - 12*np.sin(h*(np.pi/2))
x2_3 = 2*np.cos(h*(np.pi/2)) + 5*np.sin(h*(np.pi/2))
# # Part 4
x1_4 = 2*np.cos(h*(np.pi/4)) + np.sin(h*(np.pi/4))
x2_4 = np.cos(h*(np.pi/4)) - 2*np.sin(h*(np.pi/4))
# Part 5
x1_5 = 2*k - 2
x2_5 = 1*np.ones_like(k)
# Part 6
x1_6 = -2*((-0.5)**k) - 10*k*((-0.5)**k)
x2_6 = (-0.5)**k
# Part 7
x1_7 = -2*np.cos(h*(np.pi/2)) - 9*np.sin(h*(np.pi/2))
x2_7 = 2*np.cos(h*(np.pi/2)) - 8*np.sin(h*(np.pi/2))
# Part 8
x1_8 = -2*(0.5**h)
x2_8 = (-8*h-3)*(0.5)**h
# Part 9
x1_9 = 0.5*((-1)**k)*(2**k) - 0.25*(2**k)
x2_9 = ((-1)**k)*(2**k)*0.5
# # Part 10
x1_10 = np.cos(h*(np.pi/2)) + 5*np.sin(h*(np.pi/2))
x2_10 = 2*np.cos(h*(np.pi/2)) - 3*np.sin(h*(np.pi/2))
# Part 11
x1_11 = 2**h 
x2_11 = -2*(2**h) + 5*(2**h)*h
# Part 12 k = 1
x1_12 = -6*np.ones_like(k)
x2_12 = -3*np.ones_like(k)

for i in range(3):
    for j in range(4):
        Oxy(axes[i][j])

# Draw graphs of x(k) 
Draw_graphs(axes[0][0], k, x1_1, x2_1, '1', 'mediumseagreen', 'black')
Draw_graphs(axes[0][1], h, x1_2, x2_2, '2', 'mediumseagreen', 'black')
Draw_graphs(axes[0][2], h, x1_3, x2_3, '3', 'mediumseagreen', 'black')
Draw_graphs(axes[0][3], h, x1_4, x2_4, '4', 'mediumseagreen', 'black') 

Draw_graphs(axes[1][0], k, x1_5, x2_5, '5', 'mediumseagreen', 'black')
Draw_graphs(axes[1][1], k, x1_6, x2_6, '6', 'mediumseagreen', 'black')
Draw_graphs(axes[1][2], h, x1_7, x2_7, '7', 'mediumseagreen', 'black')
Draw_graphs(axes[1][3], h, x1_8, x2_8, '8', 'mediumseagreen', 'black')

Draw_graphs(axes[2][0], k, x1_9, x2_9, '9', 'mediumseagreen', 'black')
Draw_graphs(axes[2][1], h, x1_10, x2_10, '10', 'mediumseagreen', 'black') 
Draw_graphs(axes[2][2], h, x1_11, x2_11, '11', 'mediumseagreen', 'black')
Draw_graphs(axes[2][3], k, x1_12, x2_12, '12', 'mediumseagreen', 'black')

# Show graph
plt.show()
