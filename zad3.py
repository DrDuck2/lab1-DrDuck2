import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L1, L2, L3 = 2, 1.5, 1
theta1 = np.radians(30)
theta2 = np.radians(45)
theta3 = np.radians(-30)

def rotation_matrix_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def translation_matrix(tx, ty, tz):
    return np.array([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]])

M1 = rotation_matrix_z(theta1) @ translation_matrix(L1, 0, 0)
M2 = rotation_matrix_z(theta2) @ translation_matrix(L2, 0, 0)
M3 = rotation_matrix_z(theta3) @ translation_matrix(L3, 0, 0)

origin = np.array([0, 0, 0, 1])

joint0 = origin[:3]
joint1 = (M1 @ origin)[:3]
joint2 = (M1 @ M2 @ origin)[:3]
end_effector = (M1 @ M2 @ M3 @ origin)[:3]

def draw_axes(ax, length=5):
    ax.plot([0, length], [0, 0], [0, 0], 'r-', linewidth=1)  
    ax.plot([0, 0], [0, length], [0, 0], 'g-', linewidth=1)  
    ax.plot([0, 0], [0, 0], [0, length], 'b-', linewidth=1)  

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot([joint0[0], joint1[0]], [joint0[1], joint1[1]], [0, 0], 'b-', lw=3, label='Link 1')
ax.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], [0, 0], 'g-', lw=3, label='Link 2')
ax.plot([joint2[0], end_effector[0]], [joint2[1], end_effector[1]], [0, 0], 'r-', lw=3, label='Link 3')
ax.scatter(end_effector[0], end_effector[1], 0, c='magenta', s=100, label='End Effector')
draw_axes(ax)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3-Joint Robotic Arm')
ax.legend()
plt.show()
