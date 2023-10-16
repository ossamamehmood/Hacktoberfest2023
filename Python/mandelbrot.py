import numpy as np
import matplotlib.pyplot as plt

# Define the properties of the Mandelbrot Set visualization
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 256

# Create an empty image with the specified dimensions
img = np.zeros((width, height))

# Generate the Mandelbrot Set
for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break
            z = z * z + c
        # Color the pixel based on the number of iterations
        img[x, y] = i

# Create a visual representation of the Mandelbrot Set
plt.imshow(np.log(img + 1), extent=(xmin, xmax, ymin, ymax), cmap='inferno')
plt.colorbar()
plt.show()
