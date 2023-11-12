import numpy as np 
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(11, 8.5))
fig.suptitle('Exercise 5', color='green', fontname='Times New Roman', fontsize=15)

def Oxy(axes):
    plt.sca(axes)
    # Draw the coordinate system Oxy
    Ox = np.arange(-10,11,2)
    Oy = np.arange(-10,11,2)
    # Set the color for the values of the Ox axis and Oy axis
    plt.grid(linestyle="--", color="silver", linewidth=0.5)
    plt.xticks(Ox, color='black')
    plt.yticks(Oy, color='black')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # axis Ox
    plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # axis Oy

def Draw_graphs(axes, t, x1, x2, title, color_1, color_2):
    axes = plt.sca(axes)
    plt.title(f'{title}', loc='left', color='tomato')
    plt.plot(t, x1, color=f'{color_1}' , linewidth=1.25, label=r'$x_{1}(t)$') 
    plt.plot(t, x2, color=f'{color_2}' , linewidth=1.25, label=r'$x_{2}(t)$')
    plt.legend() 

t = np.arange(-10, 10, 0.05)

# Case 1
x1_1 = -np.cos(np.sqrt(10)*t) + (np.sqrt(10)/5)*np.sin(np.sqrt(10)*t)
x2_1 = 2*np.cos(np.sqrt(10)*t) + np.sqrt(10)*np.sin(np.sqrt(10)*t)
# Case 2
x1_2 = (7*t + 2)*np.exp(-t)
x2_2 = (-7*t - 5)*np.exp(-t)
# Case 3
x1_3 = (-np.pi/24)*(np.exp(-2*t) + 7*np.exp(2*t))
x2_3 = (np.pi/12)*(np.exp(-2*t) + 7*np.exp(2*t))
# Case 4
x1_4 = -np.exp(t) - np.exp(-3*t)
x2_4 = -np.exp(-t) + 3*np.exp(-3*t)



for i in range(2):
    for j in range(2):
        axes[i][j].set_xlabel('t', color='black', fontsize=12)
        axes[i][j].set_ylabel('x(t)', color='black', fontsize=12)
        axes[i][j].xaxis.set_label_coords(1.02, 0.52)
        axes[i][j].yaxis.set_label_coords(0.5, 1.016)
        axes[i][j].yaxis.label.set_rotation(0)
        Oxy(axes[i][j])
        
Draw_graphs(axes[0][0], t, x1_1, x2_1, 'Case 1', 'green', 'red')
Draw_graphs(axes[0][1], t, x1_2, x2_2, 'Case 2', 'green', 'red')
Draw_graphs(axes[1][0], t, x1_3, x2_3, 'Case 3', 'green', 'red')
Draw_graphs(axes[1][1], t, x1_4, x2_4, 'Case 4', 'green', 'red')

# Test 
# plt.sca(axes[1][1])
# plt.plot(x1_2, x2_2, color='cyan')
# plt.plot(-x1_2, -x2_2, color='cyan')

    
# Show graph
plt.show()