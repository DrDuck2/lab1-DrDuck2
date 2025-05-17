import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines

cube_points = np.array([
    [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1],
    [0, 0, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]
]).T  

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 5), (5, 6), (6, 7), (7, 4),  
    (0, 4), (1, 5), (2, 6), (3, 7)  
]

orbit_angle = np.pi / 4  

def rotation_matrix_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

R_self = rotation_matrix_z(orbit_angle)
orbit_radius = 3
T_orbit = translation_matrix(
    orbit_radius * np.cos(orbit_angle),
    orbit_radius * np.sin(orbit_angle), 
    0
)
combined = T_orbit @ R_self

transformed_cube_points = combined @ cube_points
original_points_3d = cube_points[:3, :].T
transformed_points_3d = transformed_cube_points[:3, :].T

def draw_axes(ax, length=2):
    ax.plot([0, length], [0, 0], [0, 0], 'r-', linewidth=1.5)  
    ax.plot([0, 0], [0, length], [0, 0], 'g-', linewidth=1.5)  
    ax.plot([0, 0], [0, 0], [length], 'b-', linewidth=1.5)     

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
draw_axes(ax)
for edge in edges:
    ax.plot(
        [original_points_3d[edge[0], 0], original_points_3d[edge[1], 0]],
        [original_points_3d[edge[0], 1], original_points_3d[edge[1], 1]],
        [original_points_3d[edge[0], 2], original_points_3d[edge[1], 2]],
        'b--', linewidth=1.5
    )
for edge in edges:
    ax.plot(
        [transformed_points_3d[edge[0], 0], transformed_points_3d[edge[1], 0]],
        [transformed_points_3d[edge[0], 1], transformed_points_3d[edge[1], 1]],
        [transformed_points_3d[edge[0], 2], transformed_points_3d[edge[1], 2]],
        'r-', linewidth=1.5
    )

theta = np.linspace(0, 2*np.pi, 100)
x = orbit_radius * np.cos(theta)
y = orbit_radius * np.sin(theta)
z = np.zeros_like(theta)
ax.plot(x, y, z, 'k--', alpha=0.3)

original_handle = mlines.Line2D([], [], color='blue', linestyle='--', label='Original')
transformed_handle = mlines.Line2D([], [], color='red', linestyle='-', label='Transformed')
ax.legend(handles=[original_handle, transformed_handle])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Orbiting Cube with Self-Rotation')

plt.show()