from ImgShapeBuilder import ImgShapeBuilder
from ShapeClassifier import ShapeClassifier
import os
import sys

os.system('mv new-data/* data')  # на винде не будет работать
with open("e.txt", "w") as current:
    current.write('0')
with open("t.txt", "w") as current:
    current.write('0')
with open("r.txt", "w") as current:
    current.write('0')
isb = ImgShapeBuilder("data", 28, 28)
if len(sys.argv) == 2 and sys.argv[1] == 'gen':
    isb.generate_all(100)
clf = ShapeClassifier()
clf.learn("data")
