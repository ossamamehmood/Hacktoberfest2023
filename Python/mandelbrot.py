import numpy as np
import matplotlib.pyplot as plt

x_min ,x_max = -2.5, 1.5
y_min ,y_max = -2.0, 2.0

width, height = 1000, 1000

max_iterations = 100

x_array = np.linspace(x_min, x_max, width)  # array of x and y values
y_array = np.linspace(y_min, y_max, height)

c_grid =np.array([x+y * 1j for y in y_array for x in x_array]) # 2D array of complex numbers

mandelbrot_size = np.zeros(c_grid.shape, dtype=np.uint8) # 2D array of zeros for the mandelbrot set image

for i in range(width * height):
    z = 0
    c = c_grid[i]
    for j in range(max_iterations):
        if (abs(z) > 2):
            mandelbrot_size[i] = j
            break;
        z = z**2 + c
    else: 
        mandelbrot_size[i] = max_iterations

mandelbrot_size = mandelbrot_size.reshape((height, width))

plt.imshow(mandelbrot_size, cmap='hot')
plt.show()