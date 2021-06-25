# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

from PIL import Image
from numpy import asarray, empty, append

import glob
from pathlib import Path


def get_test_data(path='.'):
    image = Image.open(path).resize((64, 64)).convert('L')
    data = asarray(image).ravel().reshape(1, -1)
    return data


def get_train_data(path='.'):
    pics = list(Path(path).glob('**/*.jpeg'))
    data = [[] for _ in range(len(pics))]
    target = []
    for i in range(len(pics)):
        image = Image.open(pics[i]).convert('L')
        data[i] = list(asarray(image).ravel())
        target += pics[i].name[0]
    return [data, target]


class ShapeClassifier:
    data = []
    target = []
    clf = []

    def __init__(self):
        pass

    def learn(self, path='.'):
        X_train, y_train = get_train_data(path)

        # Create a classifier: a support vector classifier
        self.clf = svm.SVC(gamma=0.001)

        # Learn the digits on the train subset
        self.clf.fit(X_train, y_train)

    def predict(self, path='.'):
        print(self.clf.predict(get_test_data(path)))
