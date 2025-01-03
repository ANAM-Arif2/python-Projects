# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uNM0uoxV3UxUHPPC3BSZUxfhvc17Y26-
"""

import pandas as pd
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import keras
import tensorflow as tf
import numpy as np

from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt
n = 10
plt.figure(figsize = (20,4))
for i in range(n):
    ax = plt.subplot(2, n, i+1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
plt.close()

print("x_train shape :", x_train.shape)
print("y_train shape :", y_train.shape)
print("x_test shape :", x_test.shape)
print("y_test shape :", y_test.shape)

x_train = x_train.reshape(x_train.shape[0], 28, 28,1)
x_test = x_test.reshape(x_test.shape[0], 28, 28,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = to_categorical(y_train,num_classes = 10)
y_test = to_categorical(y_test,num_classes = 10)
print("x_train shape :", x_train.shape)
print("y_train shape :", y_train.shape)
print("x_test shape :", x_test.shape)
print("y_test shape :", y_test.shape)

img_rows, img_cols, channels = 28,28,1
filters = [6,32, 80, 120]
classes = 10

from keras.models import Sequential
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D



model = Sequential()
model.add(Conv2D(filters[0], (3, 3), padding='same',
                 activation='relu', input_shape=(img_rows, img_cols, channels)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters[1], (2, 2), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters[2], (2, 2), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters[3], (2, 2), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.summary()

model.fit(x_train,y_train,validation_split = 0.2, epochs = 15, batch_size = 64, verbose = 1)

from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
y_pred_prob = model.predict(x_test, verbose=0)
y_pred = np.where (y_pred_prob>0.5, 1, 0)
test_accuracy = accuracy_score(y_pred, y_test)
print("\nTest accuracy: {}". format(test_accuracy))

mask = range(20,50)
x_valid = x_test[20:40]
actual_labels = y_test[20:40]
y_pred_probs_valid = model.predict(x_valid)
y_pred_valid = np.where(y_pred_probs_valid > 0.5, 1,0)

n = len(x_valid)
plt.figure(figsize = (20, 40))
for i in range (n):
    ax = plt.subplot(2, n, i+1)
    plt.imshow(x_valid[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    predicted_digit = np.argmax(y_pred_probs_valid[i])
    ax = plt.subplot(2, n, i+1+n)
    plt.text(0.5, 0.5, str(predicted_digit), fontsize = 12, ha= 'center', va= 'center')
    plt.axis('off')
    plt.show()
    plt.close()