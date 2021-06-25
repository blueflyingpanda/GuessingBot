from ImgShapeBuilder import ImgShapeBuilder
from ShapeClassifier import ShapeClassifier

isb = ImgShapeBuilder("data")
isb.generate_all(1000)
clf = ShapeClassifier()
clf.learn("data")
