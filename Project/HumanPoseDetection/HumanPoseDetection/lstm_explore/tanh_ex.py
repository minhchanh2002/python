import numpy as np
import matplotlib.pyplot as plt

# Step 2: Generate input values
x = np.linspace(-10, 10, 400)

# Step 3: Compute the tanh values
y = np.tanh(x)

# Step 4: Plot the graph
plt.plot(x, y)
plt.title('tanh Function')
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.grid(True)
plt.show()