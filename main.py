from ImgShapeBuilder import ImgShapeBuilder
from ShapeClassifier import ShapeClassifier
import os
import sys

os.system('mv new-data/* data')
with open("current.txt", "w") as current:
    current.write('0')
isb = ImgShapeBuilder("data", 28, 28)
if len(sys.argv) == 2 and sys.argv[1] == 'gen':
    isb.generate_all(100)
clf = ShapeClassifier()
clf.learn("data")
