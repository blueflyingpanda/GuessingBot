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
import pickle


def standartize(X):
    return (X - X.mean()) / (X.std())


def get_test_data(path='.'):
    pics = list(Path(path).glob('**/*.png'))
    data = [[] for _ in range(len(pics))]
    for i in range(len(pics)):
        image = Image.open(pics[i]).resize((28, 28)).convert('L')
        data[i] = list(standartize(asarray(image).ravel()))
    return data


def get_train_data(path='.'):
    pics = list(Path(path).glob('**/*.png'))
    data = [[] for _ in range(len(pics))]
    target = []
    for i in range(len(pics)):
        image = Image.open(pics[i]).resize((28, 28)).convert('L')
        data[i] = list(standartize(asarray(image).ravel()))
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
        self.clf = svm.SVC(gamma='scale', probability=True)

        # Learn the digits on the train subset
        self.clf.fit(X_train, y_train)
        with open('model.pkl', 'wb') as fmod:
            pickle.dump(self.clf, fmod)

    def predict(self, data):
        return [self.clf.predict(data)[0], self.clf.predict_proba(data)[0]]
