# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:57:56 2019


Kyra Lee, Silver Harris, Victoria Puck-Karam
"""
#convolutional neural network

#importing Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model


#initialize the CNN
classifier  = Sequential()

#step 1 - convlution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

#step 2 - pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#step 3 - flattening
classifier.add(Flatten())

#step 4 - full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

#compiling the CNN
classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['accuracy'])



#part 2 - fitting CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/nodule_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

test_set = test_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/nodule_test_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

from IPython.display import display
from PIL import Image

classifier.fit_generator(
    training_set,
    steps_per_epoch=8000,
    epochs=10,
    validation_data=test_set,
    validation_steps=800)

classifier.save('NoduleRemote.h5')

new_classifier = load_model('NoduleRemote.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/TestNodulePhoto.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
new_result = new_classifier.predict(test_image)
np.testing.assert_allclose(result, new_result, rtol=1e-6, atol=1e-6)
training_set.class_indices
if result[0][0] >= 0.5:
    prediction = 'No Finding'
else:
    prediction = 'Nodule Detected'
print(prediction)

if new_result[0][0] >= 0.5:
    new_prediction = 'No Finding'
else:
    new_prediction = 'Nodule Detected'
print(prediction)