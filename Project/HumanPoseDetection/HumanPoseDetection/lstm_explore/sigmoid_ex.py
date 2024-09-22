import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step 3: Generate input values
x = np.linspace(-10, 10, 400)

# Step 4: Compute the sigmoid values
y = sigmoid(x)

# Step 5: Plot the graph
plt.plot(x, y)
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.grid(True)
plt.show()