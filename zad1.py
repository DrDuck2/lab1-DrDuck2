import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines

cube_points = np.array([
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]).T 

orbit_angle = np.pi / 4 
r = 3

translation_matrix = np.array([
    [1, 0, 0, r * np.cos(orbit_angle)],
    [0, 1, 0, r * np.sin(orbit_angle)],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

c, s = np.cos(orbit_angle), np.sin(orbit_angle)
rotation_matrix = np.array([
    [c, -s, 0, 0],
    [s, c, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

combined_matrix = translation_matrix @ rotation_matrix
transformed_cube_points = combined_matrix @ cube_points
transformed_cube_points_3d = transformed_cube_points[:3, :].T

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 5), (5, 6), (6, 7), (7, 4),  
    (0, 4), (1, 5), (2, 6), (3, 7)   
]

for edge in edges:
    points = cube_points[:3, list(edge)].T
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b--')
for edge in edges:
    points = transformed_cube_points_3d[list(edge), :]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'r-')

original_handle = mlines.Line2D([], [], color='blue', linestyle='--', label='Original')
transformed_handle = mlines.Line2D([], [], color='red', linestyle='-', label='Transformed')
ax.legend(handles=[original_handle, transformed_handle])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotated and Orbiting Cube')
plt.show()