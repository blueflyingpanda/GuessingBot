from ImgShapeBuilder import ImgShapeBuilder
from ShapeClassifier import ShapeClassifier

isb = ImgShapeBuilder("data")
isb.generate_all(100)
clf = ShapeClassifier()
clf.learn("data")
