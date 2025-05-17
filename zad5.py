import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_surface(X, Y, Z, title="3D Surface Plot"):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

theta = np.linspace(0, 2 * np.pi, 60) 
h = np.linspace(0, 1, 60)  

Theta, H = np.meshgrid(theta, h)

r = 1 - H

X = r * np.cos(Theta)
Y = r * np.sin(Theta)
Z = H

plot_surface(X, Y, Z, title="Parametric Cone")
