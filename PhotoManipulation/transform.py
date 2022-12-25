from image import Image
import numpy as np

def adjust_brightness(image, factor):
    x_pixels, y_pixels,num_channels = image.array.shape
    new_image = Image(x_pixel=x_pixels, y_pixel=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = image.array[x, y, c] * factor
    return new_image


if __name__ == '__main__':
    lake = Image(filename='lake.png')
    # city = Image(filename='city.jpg')

    brightness_image = adjust_brightness(lake, 1.7)
    brightness_image.write_image('brightened.png')