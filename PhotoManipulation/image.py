import numpy as np
import png

class Image:
    def __init__(self, x_pixel=0, y_pixel=0, num_channels=0, filename=''):
        self.input_path = 'get/'
        self.output_path = 'out/'
        if x_pixel and y_pixel and num_channels:
            self.x_pixels = x_pixel
            self.y_pixels = y_pixel
            self.num_channels = num_channels
            self.array = np.zeros((x_pixel, y_pixel, num_channels))
        elif filename:
            self.array = self.read_image(filename)
            self.x_pixels, self.y_pixels , self.num_channels = self.array.shape
        else:
            raise ValueError("You need to input either a filename OR specify the dimonsies of image")
    

    def read_image(self, filename, gamma=2.2):
        image = png.Reader(self.input_path+filename).asFloat()
        resized_image = np.vstack(list(image[2]))
        resized_image.resize(image[1], image[0], 3)
        resized_image = resized_image ** gamma
        return resized_image

    def write_image(self, output_file, gamma=2.2):
        image = np.clip(self.array, 0, 1)
        y, x = self.array.shape[0], self.array.shape[1]
        image = image.reshape(y, x * 3)
        writer = png.Writer(x, y)

        with open(self.output_path + output_file, 'wb') as f:
            writer.write(f, 255*(image ** (1/gamma)))

        self.array.resize(y, x, 3)
    
if __name__ == '__main__':
    image = Image(filename='lake.jpg')
    image.write_image('lake_update.png')