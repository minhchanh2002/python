import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import MaxPooling2D

# Load a local image
image_path = 'E:/images/elephant.jpg'  # Replace with the path to your local image
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
image = tf.keras.preprocessing.image.img_to_array(image)
image = np.expand_dims(image, axis=0)  # Add batch dimension

# Define a max pooling layer
max_pool_layer = MaxPooling2D(pool_size=(2, 2))

# Apply the max pooling layer to the original image
pooled_image = max_pool_layer(image)
pooled_image = tf.squeeze(pooled_image, axis=0)  # Remove batch dimension

# Display the original image and the pooled image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image[0].astype('uint8'))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Pooled Image')
plt.imshow(pooled_image.numpy().astype('uint8'))
plt.axis('off')

plt.show()