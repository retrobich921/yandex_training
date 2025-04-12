import numpy as np


def compute_sobel_gradients_two_loops(image):
    height, width = image.shape

    gradient_x = np.zeros_like(image, dtype=np.float64)
    gradient_y = np.zeros_like(image, dtype=np.float64)

    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant', constant_values=0)

    sobel_x = np.array([[-1, 0, 1], 
                       [-2, 0, 2], 
                       [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]])

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            gradient_x[i-1][j-1] = sum(padded_image[y + i][x + j] * sobel_x[y + 1][x + 1] for y in range(-1, 2) for x in range(-1, 2))
            gradient_y[i-1][j-1] = sum(padded_image[y + i][x + j] * sobel_y[y + 1][x + 1] for y in range(-1, 2) for x in range(-1, 2))

    return gradient_x, gradient_y


def compute_gradient_magnitude(sobel_x, sobel_y):

    magnitude = np.zeros((28, 28))

    for i in range(28):
        for j in range(28):
            magnitude[i][j] = np.sqrt(sobel_x[i][j]**2 + sobel_y[i][j]**2)

    return magnitude


def compute_gradient_direction(sobel_x, sobel_y):

    gradient_direction = np.zeros((28, 28))
    
    for i in range(28):
        for j in range(28):
            gradient_direction[i][j] = np.degrees(np.arctan2(sobel_y[i][j], sobel_x[i][j]))
            
    return gradient_direction


def compute_hog(image, pixels_per_cell=(cell_size, cell_size), bins=9):
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)
    
    gradient_x, gradient_y = compute_sobel_gradients_two_loops(image)

    magnitude = compute_gradient_magnitude(gradient_x, gradient_y)
    direction = compute_gradient_direction(gradient_x, gradient_y)

    cell_height, cell_width = pixels_per_cell
    n_cells_x = image.shape[1] // cell_width
    n_cells_y = image.shape[0] // cell_height

    histograms = np.zeros((n_cells_y, n_cells_x, bins))
    bin_width = 360.0 / bins

    for i in range(n_cells_y):
        for j in range(n_cells_x):
            cell_magnitude = magnitude[i * cell_height : (i+1) * cell_height, 
                                       j * cell_width  : (j+1) * cell_width]
            cell_direction = direction[i * cell_height : (i+1) * cell_height, 
                                       j * cell_width  : (j+1) * cell_width]
            cell_hist = np.zeros(bins)
            for y in range(cell_height):
                for x in range(cell_width):
                    
                    bin_ind = int((cell_direction[y][x] + 180) // bin_width if cell_direction[y][x] + 180 < 360 else bins - 1)
                    cell_hist[bin_ind] += cell_magnitude[y][x]

            if cell_hist.sum() > 0:
                cell_hist /= cell_hist.sum()
            histograms[i, j, :] = cell_hist
    
    return histograms