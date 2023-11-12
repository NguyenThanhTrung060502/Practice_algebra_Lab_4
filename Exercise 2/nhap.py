import numpy as np
import matplotlib.pyplot as plt

def Oxy():
	# Draw the coordinate system Oxy
    Ox = np.arange(-10,11,2)
    Oy = np.arange(-10,11,2)
    # Set the color for the values of the Ox axis and Oy axis
    plt.xticks(Ox, color='black')
    plt.yticks(Oy, color='black')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # axis Ox
    plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # axis Oy

# Задание временного интервала
t = np.arange(-10, 10, 0.01)

# Вычисление значений x1 и x2
# x(0) = [2 1]
x1 = np.exp(t) + np.exp(-t)
x2 = np.exp(-t)
# x(0) = [1 0] = v1
z1 = np.exp(t)
z2 = np.zeros_like(t)
# x(0) = [1 1] = v2
t1 = np.exp(-t)
t2 = np.exp(-t)

# x(0) = [-1 3]
y1 = -4*np.exp(t) + 3*np.exp(-t)
y2 = 3*np.exp(-t)
# x(0) = [-2 -3]
g1 = np.exp(t) - 3*np.exp(-t)
g2 = - 3*np.exp(-t)

# Построение фазовой траектории
plt.plot(x1, x2, color='black')
plt.plot(z1, z2, color='red')
plt.plot(t1, t2, color='blue')
# Vẽ đối xứng qua tâm O 
plt.plot(-x1, -x2, color='black')
plt.plot(-z1, -z2, color='red')
plt.plot(-t1, -t2, color='blue')

plt.plot(y1, y2, color='black')
plt.plot(g1, g2, color='black')
# Vẽ đối xứng qua tâm O 
plt.plot(-y1, -y2, color='black')
plt.plot(-g1, -g2, color='black')

Oxy()

plt.title('Phase Trajectory')
plt.grid(True)
plt.show()