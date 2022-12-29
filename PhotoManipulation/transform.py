from image import Image
import numpy as np

def adjust_brightness(image, factor):
    x_pixels, y_pixels,num_channels = image.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_image.array[x, y, c] = image.array[x, y, c] * factor
    new_image.array = image.array * factor
    return new_image

def adjust_contrast(image, factor, mid=0.5):
    x_pixels, y_pixels,num_channels = image.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid
    return new_image

def blur(image, kernel_size):
    x_pixels, y_pixels,num_channels = image.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x-neighbor_range), min(x_pixels - 1, x+neighbor_range) + 1):
                    for y_i in range(max(0, y-neighbor_range), min(y_pixels - 1, y+neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]
                new_image.array[x,y,c] = total / (kernel_size ** 2)
    return new_image

def apply_kernel(image, kernel):
    x_pixels, y_pixels,num_channels = image.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size //2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x-neighbor_range), min(x_pixels - 1, x+neighbor_range) + 1):
                    for y_i in range(max(0, y-neighbor_range), min(y_pixels - 1, y+neighbor_range) + 1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_image.array[x, y, c] = total
    return new_image


def combine_images(image1, image2):
    x_pixels, y_pixels,num_channels = image1.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = (image1.array[x,y,c]**2 + image2.array[x,y,c]**2)**0.5
    return new_image

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')
    # city = Image(filename='city.jpg')

    # brightness_image = adjust_brightness(lake, 0.3)
    # brightness_image.write_image('darkened.png')

    # increment_contrast = adjust_contrast(lake, 2)
    # increment_contrast.write_image('increases_contrast.jpg')

    # decrement_contrast = adjust_contrast(lake, 0.5)
    # decrement_contrast.write_image('decrease_contrast.jpg')

    # blur_03 = blur(city, 3)
    # blur_03.write_image('blur_city_3.png')
    
    # blur_15 = blur(city, 15)
    # blur_15.write_image('blur_city_15.png')

    #apply a sobel edge detection kernel

    sobel_x_kernel = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])

    sobel_y_kernel = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])


    sobel_x = apply_kernel(city, sobel_x_kernel)
    # sobel_x.write_image('edge_x.png')
    sobel_y = apply_kernel(city, sobel_y_kernel)
    # sobel_y.write_image('edge_y.png')
    sobel = combine_images(sobel_x, sobel_y)
    sobel.write_image('combined_images.png')

