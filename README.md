# inverse-pendulum-control
The integration of a controller to stabilize an inverted pendulum on a motorized cart.

# Theory
The necessary theoretical background for this project can be found [here](./Documents/Control_theory.pdf).

# Report
The aim of this project is to integrate a controller for an inverted pendulum through the use of state-space representation of the system, and through linearization techniques.

## MATLAB code
The steps performed to create the controller are explained in details in the main MATLAB [file](./src/main.mlx). The file is in Live Script format and requires MATLAB to be compiled and executed together with the simulation on Simulink. A pdf version of the main file was therefore exported and is available for reading [here](./Documents/Report.pdf).

## Simulink simulations
The simulation model made with Simulink is the following:
![Sim Graph](./Documents/images/sim_graph.png?raw=true "Simulation graph")
For convenience, the user gets to choose between setting the target through MATLAB code or by hand using three blocks.

## Simulation results
The scope shows the computed parameters over time. We will now list results based on the target values given.

Note: The x axis is time in seconds (0 to 5), while the y axis is units of length for the translation variable X, and degrees for variable th.

The variable X is the position of the cart from the origin, dX and ddX being its derivatives (respectively velocity and acceleration). The variable th is the angle of the pendulum from the vertical. dth and ddth are its derivatives as well (respectively angular velocity and angular acceleration). We only show X, dX, th, and dth, as the acceleration amplitudes hinder the examination of other data.

The initial conditions will always be the same in simulation:
- X0 = -10; dX0 = -7; th0 = 6; dth0 = 0

Let's now plot the simulation results at different targets.

### Equilibrium point: X = 0; dX = 0; th = 0; dth = 0
![Sim Graph](./Documents/images/0_0_0_0.png?raw=true "Equilibrium point")
The inverted pendulum manages to stabilize around the equilibrium point in less than 10 seconds.

### Specific coordinates: X = 7; dX = 0; th = 0; dth = 0
![Sim Graph](./Documents/images/7_0_0_0.png?raw=true "Specific coordinate")
The inverted pendulum manages to stabilize around the equilibrium point at coordinates that differ from 0.

### Specific velocity: X = free; dX = 1; th = 0; dth = 0
![Sim Graph](./Documents/images/f_1_0_0.png?raw=true "Specific velocity")
The inverted pendulum manages to stabilize around the equilibrium point while reaching and keeping a fixed velocity.

### Free translation: X = free; dX = free; th = 0; dth = 0
![Sim Graph](./Documents/images/f_f_0_0.png?raw=true "Free translation")
The inverted pendulum manages to stabilize around the equilibrium point quickly, but the velocity and acceleration are unrealistic.

# Conclusion
In conclusion, this MATLAB/Simulink project successfully demonstrated the control of an inverted pendulum, with conclusive results that validate the applied control strategies. The detailed explanations of the design process, from modeling the system dynamics to implementing the controller, provide a solid foundation for understanding control theory. This work not only showcases the practical application of control concepts but also serves as a valuable resource for future engineers seeking to deepen their knowledge in dynamic systems and feedback control.