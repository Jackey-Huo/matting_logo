from PIL import Image
from PIL import ImageDraw

img = Image.open("skyworks.png")
width = img.width
height = img.height
canvas = Image.new("RGBA", [width, height], (255, 255, 255, 255))

R = 0 G = 1 B = 2
A = 3

for x in range(width):
    for y in range(height):
        rgba = img.getpixel((x, y))
        if rgba[R] >= 230 and rgba[G] >= 230 and rgba[B] >= 230:
                canvas.putpixel((x, y), (0, 0, 0, 0))
        else:
                canvas.putpixel((x, y), (rgba[R], rgba[G], rgba[B], 255))


canvas.save("skyworks3.png")

