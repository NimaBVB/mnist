# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from keras.datasets import mnist
(train_X, train_y), (test_X, test_y) = mnist.load_data()

pixels = train_X[1]
plt.grid()
for i in range(28):
    for j in range(28): 
        plt.scatter(i,j, s = pixels[i,j])
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()

