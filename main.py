from ImgShapeBuilder import ImgShapeBuilder

import telebot

import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

isb = ImgShapeBuilder("data")
isb.generate_all(100)
bot = telebot.TeleBot('1855857929:AAH-r1NKWky7sM459iIdWrlI12EvUuOyHLM')
