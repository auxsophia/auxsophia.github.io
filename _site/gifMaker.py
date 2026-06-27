from PIL import Image
from random import random

width = 128
height = 128
num_images = 100
images = []

for i in range(num_images):
    data = []
    for h in range(height):
        for w in range(width):
            if random() >= 0.5:
                data += [255]
            else:
                data += [0]

    # https://stackoverflow.com/questions/58297585/how-do-i-create-and-save-gif-of-gray-scale-images-with-pillow
    # Note that GIF files are always read as grayscale ('L') or palette mode ('P') images.
    img = Image.new('1', (width, height)).convert('P')
    img.putdata(data)
    images.append(img.copy())

#images[0].show()
#img.save('image.png')

# Make gifs: https://stackoverflow.com/questions/24688802/saving-an-animated-gif-in-pillow
images[0].save('static_snow.gif', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)

# Black and white 1
data = []
for h in range(height):
    for w in range(width):
        if w > (width*0.4) and w < (width*0.6) and h > (height*0.2) and h < (height*0.8):
            data += [255]
        else:
            data += [0]

img = Image.new('1', (width, height)).convert('P')
img.putdata(data)

num_images = 10
images = [img]

for i in range(num_images):
    data = []
    for h in range(height):
        for w in range(width):
            if random() >= 0.5:
                data += [255]
            else:
                data += [0]

    # https://stackoverflow.com/questions/58297585/how-do-i-create-and-save-gif-of-gray-scale-images-with-pillow
    # Note that GIF files are always read as grayscale ('L') or palette mode ('P') images.
    img = Image.new('1', (width, height)).convert('P')
    img.putdata(data)
    images.append(img.copy())

images[0].save('static1.gif', save_all=True, append_images=images[1:], optimize=False, duration=111, loop=0)
