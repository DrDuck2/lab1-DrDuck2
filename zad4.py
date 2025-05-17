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

n1, n2 = 5, 5

def superellipsoid(u, v, a=1, b=1, c=1):
    cosu = np.cos(u)
    sinu = np.sin(u)
    cosv = np.cos(v)
    sinv = np.sin(v)

    def sgn(x): return np.sign(x)
    def exp(x, n): return sgn(x) * (np.abs(x) ** n)

    x = a * exp(cosu, n1) * exp(cosv, n2)
    y = b * exp(sinu, n1) * exp(cosv, n2)
    z = c * exp(sinv, n2)
    return x, y, z

u = np.linspace(-np.pi, np.pi, 60)
v = np.linspace(-np.pi/2, np.pi/2, 60)
U, V = np.meshgrid(u, v)
X, Y, Z = superellipsoid(U, V)
plot_surface(X, Y, Z, title="Parametric Superellipsoid")


# n1 = 0.5, n2 = 0.5 -> Cuboid/box like shape
# n1 = 1, n2 = 1 -> Smooth sphere, like a ball
# n1 = 5, n2 = 5 -> Star-like shape, with sharp indentations

# n1 -> controls curvature along the longitude
# n2 -> controls curvature along the latitude