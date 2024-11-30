import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Initial missile/bomb parameters
mass = 230  # Mass of the bomb (kg)
area = 0.25  # Reference area (m^2)
air_density = 1.225  # Air density (kg/m^3)
gravity = 9.81  # Gravity (m/s^2)

# Aerodynamic coefficients
C_x = 0.5  # Drag coefficient in X
C_y = 0.05  # Drag coefficient in Y
C_z = 0.4  # Drag coefficient in Z

# Initial conditions
initial_speed = 250  # Initial speed (m/s)
initial_height = 5000  # Initial height (m)
launch_angle_deg = 60  # Initial launch angle (degrees)
deviation_angle_deg = 45  # Initial horizontal deviation angle (degrees)
wind_speed = 10  # Wind speed in Y (m/s)
radar_range = 20000  # Radar detection range (m)

# Convert angles to radians
launch_angle = np.radians(launch_angle_deg)  # Vertical angle
deviation_angle = np.radians(deviation_angle_deg)  # Horizontal angle

# Initialize variables
u = initial_speed * np.cos(launch_angle) * np.cos(deviation_angle)  # Initial velocity component in X
v = initial_speed * np.cos(launch_angle) * np.sin(deviation_angle) + wind_speed  # Initial velocity component in Y
w = initial_speed * np.sin(launch_angle)  # Initial velocity component in Z
x, y, z = 0, 0, initial_height  # Initial position

# Store results
trajectory = {'x': [x], 'y': [y], 'z': [z], 'u': [u], 'v': [v], 'w': [w]}

# Functions to calculate accelerations and navigation
def calculate_accelerations(u, v, w, air_density, area, mass):
    V = np.sqrt(u**2 + v**2 + w**2)  # Total velocity
    du_dt = (-C_x * 0.5 * air_density * V**2 * area) / mass
    dv_dt = (-C_y * 0.5 * air_density * V**2 * area) / mass
    dw_dt = (-gravity - C_z * 0.5 * air_density * V**2 * area) / mass
    return du_dt, dv_dt, dw_dt

def calculate_navigation(u, v, w):
    dx_dt = u
    dy_dt = v
    dz_dt = w
    return dx_dt, dy_dt, dz_dt

# Simulation
dt = 0.01  # Time step (s)
t_max = 60  # Maximum time (s)

for t in np.arange(0, t_max, dt):
    if z <= 0:
        break

    du_dt, dv_dt, dw_dt = calculate_accelerations(u, v, w, air_density, area, mass)

    # Update velocities
    u += du_dt * dt
    v += dv_dt * dt
    w += dw_dt * dt

    dx_dt, dy_dt, dz_dt = calculate_navigation(u, v, w)

    x += dx_dt * dt
    y += dy_dt * dt
    z += dz_dt * dt

    trajectory['x'].append(x)
    trajectory['y'].append(y)
    trajectory['z'].append(z)
    trajectory['u'].append(u)
    trajectory['v'].append(v)
    trajectory['w'].append(w)

x_vals = np.array(trajectory['x'])
y_vals = np.array(trajectory['y'])
z_vals = np.array(trajectory['z'])
u_vals = np.array(trajectory['u'])
v_vals = np.array(trajectory['v'])
w_vals = np.array(trajectory['w'])
speed = np.sqrt(u_vals**2 + v_vals**2 + w_vals**2)
angle_change = np.degrees(np.arctan2(w_vals, np.sqrt(u_vals**2 + v_vals**2)))

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, np.max(x_vals) * 1.5)
ax.set_ylim(np.min(y_vals) * 1.5, np.max(y_vals) * 1.5)
ax.set_zlim(0, initial_height * 2)

# Axis labels
ax.set_xlabel('Distance X (m)')
ax.set_ylabel('Distance Y (m)')
ax.set_zlabel('Height Z (m)')
ax.set_title('Missile Simulation in 3D Space with Radar Detection (Expanded Range)')

cube_x = [0, np.max(x_vals) * 1.5, np.max(x_vals) * 1.5, 0, 0, np.max(x_vals) * 1.5, np.max(x_vals) * 1.5, 0]
cube_y = [np.min(y_vals) * 1.5, np.min(y_vals) * 1.5, np.max(y_vals) * 1.5, np.max(y_vals) * 1.5,
          np.min(y_vals) * 1.5, np.min(y_vals) * 1.5, np.max(y_vals) * 1.5, np.max(y_vals) * 1.5]
cube_z = [0, 0, 0, 0, initial_height * 2, initial_height * 2, initial_height * 2, initial_height * 2]
cube_plot = ax.plot_trisurf(cube_x, cube_y, cube_z, color='blue', alpha=0.1)

xx, yy = np.meshgrid(
    np.linspace(0, np.max(x_vals), 50),
    np.linspace(np.min(y_vals), np.max(y_vals), 50)
)
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2, color='green')  # Represents the ground
ax.scatter(15000, 8000, 0, color='red', label='Target', s=200)  # Target

line, = ax.plot([], [], [], lw=2, color='cyan', label="Trajectory")
point, = ax.plot([], [], [], 'o', color='red', label="Missile")
text_pos = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)
text_vel = ax.text2D(0.05, 0.90, "", transform=ax.transAxes)
text_angle = ax.text2D(0.05, 0.85, "", transform=ax.transAxes)

# Initialization function
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    text_pos.set_text('')
    text_vel.set_text('')
    text_angle.set_text('')
    return line, point, text_pos, text_vel, text_angle

# Update function
def update(frame):
    global cube_plot
    line.set_data(x_vals[:frame], y_vals[:frame])
    line.set_3d_properties(z_vals[:frame])
    point.set_data([x_vals[frame]], [y_vals[frame]])
    point.set_3d_properties([z_vals[frame]])

    pos_text = f"Position: X={x_vals[frame]:.2f} m, Y={y_vals[frame]:.2f} m, Z={z_vals[frame]:.2f} m"
    vel_text = f"Speed: {speed[frame]:.2f} m/s"
    angle_text = f"Angle: {angle_change[frame]:.2f}°"
    text_pos.set_text(pos_text)
    text_vel.set_text(vel_text)
    text_angle.set_text(angle_text)

    if (x_vals[frame] > ax.get_xlim()[1] or
        y_vals[frame] > ax.get_ylim()[1] or
        z_vals[frame] > ax.get_zlim()[1]):

        # Expand cube limits
        ax.set_xlim(0, x_vals[frame] * 1.5)
        ax.set_ylim(np.min(y_vals) * 1.5, y_vals[frame] * 1.5)
        ax.set_zlim(0, z_vals[frame] * 1.5)

        cube_x = [0, x_vals[frame] * 1.5, x_vals[frame] * 1.5, 0, 0, x_vals[frame] * 1.5, x_vals[frame] * 1.5, 0]
        cube_y = [np.min(y_vals) * 1.5, np.min(y_vals) * 1.5, y_vals[frame] * 1.5, y_vals[frame] * 1.5,
                  np.min(y_vals) * 1.5, np.min(y_vals) * 1.5, y_vals[frame] * 1.5, y_vals[frame] * 1.5]
        cube_z = [0, 0, 0, 0, z_vals[frame] * 1.5, z_vals[frame] * 1.5, z_vals[frame] * 1.5, z_vals[frame] * 1.5]

        cube_plot.remove()
        cube_plot = ax.plot_trisurf(cube_x, cube_y, cube_z, color='blue', alpha=0.1)

    return line, point, text_pos, text_vel, text_angle

ani = FuncAnimation(fig, update, frames=len(x_vals), init_func=init, blit=False, interval=20)

plt.legend()
plt.show()
