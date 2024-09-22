import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y)
def f(x, y):
    return x**2 * y

# Compute the partial derivatives
def df_dx(x, y):
    return 2 * x * y

def df_dy(x, y):
    return x**2

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute the function values and partial derivatives on the grid
Z = f(X, Y)
dZ_dx = df_dx(X, Y)
dZ_dy = df_dy(X, Y)

# Plot the function f(x, y)
fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('f(x, y) = x^2 * y')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# Plot the partial derivative with respect to x
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, dZ_dx, cmap='viridis')
ax2.set_title('∂f/∂x = 2xy')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('∂f/∂x')

# Plot the partial derivative with respect to y
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, dZ_dy, cmap='viridis')
ax3.set_title('∂f/∂y = x^2')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('∂f/∂y')

plt.show()