import tensorflow as tf

# Example values for f_t, C_prev, i_t, and C_tilde
f_t = tf.constant([[0.5, 0.6], [0.7, 0.8]], dtype=tf.float32)
C_prev = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
i_t = tf.constant([[0.1, 0.2], [0.3, 0.4]], dtype=tf.float32)
C_tilde = tf.constant([[0.9, 1.0], [1.1, 1.2]], dtype=tf.float32)

# Compute C_t
C_t = f_t * C_prev + i_t * C_tilde

# Define a simple loss function (sum of all elements in C_t)
with tf.GradientTape() as tape:
    tape.watch([f_t, C_prev, i_t, C_tilde])
    loss = tf.reduce_sum(C_t)

# Compute the gradients of the loss with respect to f_t, C_prev, i_t, and C_tilde
gradients = tape.gradient(loss, [f_t, C_prev, i_t, C_tilde])

# Print the gradients
print("C_t:")
print(C_t.numpy())
print("\nGradients with respect to f_t:")
print(gradients[0].numpy())
print("\nGradients with respect to C_prev:")
print(gradients[1].numpy())
print("\nGradients with respect to i_t:")
print(gradients[2].numpy())
print("\nGradients with respect to C_tilde:")
print(gradients[3].numpy())