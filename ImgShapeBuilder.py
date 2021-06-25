from PIL import Image, ImageDraw
import random

'''
ImgShapeBuilder is used to create arbitrary images of size 64px,64px of shapes (triangles, rectangles, ellipses) for data-set.
When constructing specify path for saving images.
shapes will be saved in .jpeg according to the convention:
    triangles -> tria#.jpeg
    rectangles -> rect#.jpeg
    ellipses -> circ#.jpeg
    '#' will be replaced with image number starting from 0
Running the ImgShapeBuilder methods again at the same path will result in overwriting previous images
Pillow (PIL) library is required for drawing
Path should be valid!
'''


class ImgShapeBuilder:
    path = '.'
    w, h = 64, 64

    def __init__(self, path='.'):
        self.path = path

    def generate_rectangles(self, amount=10):
        for i in range(0, amount):
            shape = [(random.randint(8, 24), random.randint(8, 24)), (random.randint(40, 56), random.randint(40, 56))]

            # creating new Image object
            img = Image.new("RGB", (self.w, self.h), (255, 255, 255))

            # create rectangle image
            img1 = ImageDraw.Draw(img)
            img1.rectangle(shape, outline="black", width=random.randint(3, 6))
            if random.randint(0, 1):
                if random.randint(0, 1):
                    img = img.rotate(random.randint(0, 45), fillcolor=(255, 255, 255))
                else:
                    img = img.rotate(random.randint(314, 359), fillcolor=(255, 255, 255))
            img.save(self.path + "/rect" + str(i) + ".jpeg")

    def generate_ellipses(self, amount=10):
        for i in range(0, amount):
            shape = [(random.randint(8, 24), random.randint(8, 24)), (random.randint(40, 56), random.randint(40, 56))]

            # creating new Image object
            img = Image.new("RGB", (self.w, self.h), (255, 255, 255))

            # create ellipse image
            img1 = ImageDraw.Draw(img)
            img1.ellipse(shape, outline="black", width=random.randint(3, 6))
            img.save(self.path + "/circ" + str(i) + ".jpeg")

    def generate_triangles(self, amount=10):
        for i in range(0, amount):
            entry_point = (random.randint(8, 24), random.randint(8, 24))
            shape = [entry_point, (random.randint(40, 56), random.randint(8, 24)),
                     (random.randint(8, 56), random.randint(40, 56)), entry_point]

            # creating new Image object
            img = Image.new("RGB", (self.w, self.h), (255, 255, 255))

            # create triangle image
            img1 = ImageDraw.Draw(img)
            img1.line(shape, fill="black", width=random.randint(3, 6))
            if random.randint(0, 1):
                img = img.rotate(180)
            img.save(self.path + "/tria" + str(i) + ".jpeg")

    def generate_all(self, amount=10):
        self.generate_triangles(amount)
        self.generate_rectangles(amount)
        self.generate_ellipses(amount)
