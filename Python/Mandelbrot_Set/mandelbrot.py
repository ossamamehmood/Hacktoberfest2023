import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            img[i, j] = mandelbrot(complex(x[i], y[j]), max_iter)

    return img

if __name__ == "__main__":
    # Define the image dimensions and the range in the complex plane
    width, height = 800, 800
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    max_iter = 256

    # Generate the Mandelbrot Set
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    # Display the Mandelbrot Set using matplotlib
    plt.imshow(mandelbrot_image.T, extent=(xmin, xmax, ymin, ymax), cmap="hot", origin="lower")
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()
