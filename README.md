Missile Flight Simulation
Created by: Ilyes Ameraoui

This repository contains a Python simulation for modeling the 3D flight trajectory of a missile or bomb, considering factors such as gravitational forces, air resistance (drag), and wind speed. The simulation includes an animated 3D visualization of the missile’s flight path, which dynamically updates in real-time as it moves through the air. You can adjust key parameters like the launch angle, wind speed, and mass to simulate various scenarios.

Overview
The simulation models a missile’s motion in 3D space, using realistic physics based on the following:

Gravitational acceleration (g = 9.81 m/s²)
Air drag, based on the drag coefficient (Cd)
Wind speed
Initial launch velocity and angle
The missile is animated, and real-time information is displayed on the screen, such as its position and the time elapsed. The missile’s path is visualized in a 3D plot, and the system includes a radar detection range around the missile for visualization purposes.

Features
3D Flight Path Visualization: See the missile's trajectory in 3D, with distance on the X, Y, and Z axes.
Real-Time Animation: The missile's movement is animated over time with its position updated dynamically.
Radar Detection: A radar range is displayed as a cube around the missile, representing the detection zone.
Customizable Parameters: Easily adjust the launch parameters like velocity, angle, wind speed, and mass.
Realistic Physics: The simulation takes into account air drag, gravitational forces, and wind effects on the missile's flight.
Key Parameters
1. Mass (kg)
Description: Mass of the missile or bomb.
Default: 230 kg.
2. Reference Area (m²)
Description: The effective surface area exposed to aerodynamic drag.
Default: 0.25 m².
3. Air Density (kg/m³)
Description: The density of air in the environment through which the missile travels.
Default: 1.225 kg/m³.
4. Gravitational Acceleration (m/s²)
Description: The gravitational constant that influences the missile’s fall.
Default: 9.81 m/s².
5. Drag Coefficients
Description: Coefficients that represent air drag in the X, Y, and Z directions:
Cd_X: Drag coefficient in the horizontal direction.
Cd_Y: Drag coefficient in the direction of the wind.
Cd_Z: Drag coefficient in the vertical direction.
Defaults:
Cd_X = 0.5
Cd_Y = 0.05
Cd_Z = 0.4
6. Initial Velocity (m/s)
Description: The initial velocity at which the missile is launched.
Default: 250 m/s.
7. Launch Angles
Theta (°): Vertical launch angle (from horizontal).
Default: 60°.
Phi (°): Horizontal launch angle (side-to-side deviation).
Default: 45°.
8. Wind Speed (m/s)
Description: Speed of wind affecting the missile’s horizontal motion.
Default: 10 m/s.
9. Radar Detection Range (m)
Description: The distance at which the missile can be detected by radar.
Default: 20,000 meters.
Usage
To run the missile flight simulation, follow the steps below:

Requirements
Python 3.x: The program is written in Python and requires Python 3.x.
Dependencies:
numpy for numerical calculations.
matplotlib for 3D plotting and animation.
To install the required dependencies, use the following:

bash
Copiar código
pip install numpy matplotlib
Running the Script
Clone the repository to your local machine:
bash
Copiar código
git clone https://github.com/ilyesameraoui/missile-flight-simulation.git
Navigate into the project directory:
bash
Copiar código
cd missile-flight-simulation
Run the Python script:
bash
Copiar código
python missile_simulation.py
This will generate a real-time animation of the missile's flight path, showing its position and the environment’s influence on its trajectory.

How to Modify the Simulation
To adjust the missile's flight parameters:

Change the Launch Angle (Theta and Phi):

Modify the values of initial_theta and initial_phi to simulate different launch angles.
python
Copiar código
initial_theta = 60  # Launch angle from horizontal (degrees)
initial_phi = 45    # Horizontal deviation angle (degrees)
Adjust Wind Speed:

Modify the wind_speed parameter to simulate different wind conditions.
python
Copiar código
wind_speed = 10  # Wind speed in m/s
Set Initial Velocity:

Adjust the initial_velocity for different initial speeds.
python
Copiar código
initial_velocity = 250  # Initial velocity in m/s
Example Scenario
You can modify the code to simulate different flight conditions. For instance:

Scenario 1: No wind, low launch velocity:

python
Copiar código
wind_speed = 0
initial_velocity = 150  # Lower velocity
Scenario 2: High wind speed and steep launch angle:

python
Copiar código
wind_speed = 50  # Strong wind
initial_theta = 75  # Steeper launch angle
Output
Once the script is executed, the following outputs will be displayed:

3D Visualization: A plot showing the missile's trajectory in 3D space (X, Y, Z).
Radar Detection Range: A cube representing the radar's detection zone around the missile.
Animation: A dynamic animation of the missile’s flight path, updating its position frame by frame.
Dynamic Information: Real-time updates of missile’s position and time elapsed in the simulation.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to contact the creator:

Email: ilyes.ameraoui@example.com
GitHub: ilyesameraoui
