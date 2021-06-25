from PIL import Image, ImageDraw
import random

'''
ImgShapeBuilder is used to create arbitrary images of shapes (triangles, rectangles, ellipses) for data-set.
When constructing specify path for saving images.
shapes will be saved in .png according to the convention:
    triangles -> tria#.png
    rectangles -> rect#.png
    ellipses -> circ#.png
    '#' will be replaced with image number starting from 0
Running the ImgShapeBuilder methods again at the same path will result in overwriting previous images
Pillow (PIL) library is required for drawing
Path should be valid!
'''


class ImgShapeBuilder:
    path = '.'
    width, height = 64, 64

    def __init__(self, path='.', width=64, height=64):
        self.path = path
        self.width, self.height = width, height

    def generate_rectangles(self, amount=10):
        for i in range(0, amount):
            shape = [(random.randint(self.width//8, self.width//8*3), random.randint(self.height//8, self.height//8*3)),
                     (random.randint(self.width//8*5, self.width//8*7),
                      random.randint(self.height//8*5, self.height//8*7))]

            # creating new Image object
            img = Image.new("RGB", (self.width, self.height), (255, 255, 255))

            # create rectangle image
            img1 = ImageDraw.Draw(img)
            img1.rectangle(shape, outline="black", width=random.randint(3, 6))
            if random.randint(0, 1):
                if random.randint(0, 1):
                    img = img.rotate(random.randint(0, 45), fillcolor=(255, 255, 255))
                else:
                    img = img.rotate(random.randint(314, 359), fillcolor=(255, 255, 255))
            img.save(self.path + "/rect" + str(i) + ".png")

    def generate_ellipses(self, amount=10):
        for i in range(0, amount):
            shape = [(random.randint(self.width//8, self.width//8*3), random.randint(self.height//8, self.height//8*3)),
                     (random.randint(self.width//8*5, self.width//8*7),
                      random.randint(self.height//8*5, self.height//8*7))]

            # creating new Image object
            img = Image.new("RGB", (self.width, self.height), (255, 255, 255))

            # create ellipse image
            img1 = ImageDraw.Draw(img)
            img1.ellipse(shape, outline="black", width=random.randint(3, 6))
            img.save(self.path + "/circ" + str(i) + ".png")

    def generate_triangles(self, amount=10):
        for i in range(0, amount):
            entry_point = (random.randint(self.width//8, self.width//8*3),
                           random.randint(self.height//8, self.height//8*3))
            shape = [entry_point, (random.randint(self.width//8*5, self.width//8*7),
                                   random.randint(self.height//8, self.height//8*3)),
                     (random.randint(self.width//8, self.width//8*7),
                      random.randint(self.height//8*5, self.height//8*7)), entry_point]

            # creating new Image object
            img = Image.new("RGB", (self.width, self.height), (255, 255, 255))

            # create triangle image
            img1 = ImageDraw.Draw(img)
            img1.line(shape, fill="black", width=random.randint(3, 6))
            if random.randint(0, 1):
                img = img.rotate(180)
            img.save(self.path + "/tria" + str(i) + ".png")

    def generate_all(self, amount=10):
        self.generate_triangles(amount)
        self.generate_rectangles(amount)
        self.generate_ellipses(amount)
