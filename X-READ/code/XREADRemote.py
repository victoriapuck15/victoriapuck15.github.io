# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:41:01 2019

@author: 1439208
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:24:25 2019

@author: 1439208
"""
from keras.models import load_model
from keras.models import Sequential


import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
#mass test
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)
training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/mass_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
mass_classifier = Sequential()
mass_classifier = load_model('MassRemote.h5')
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/ObviousMass.PNG', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
mass_result = mass_classifier.predict(test_image)
training_set.class_indices
if mass_result[0][0] >= 0.5:
    mass_prediction = 'No Finding'
else:
    mass_prediction = 'Mass Detected'
print(mass_prediction)

#nodule test
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)
training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/nodule_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
mass_classifier = Sequential()
mass_classifier = load_model('NoduleRemote.h5')
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/TestNodulePhoto.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
mass_result = mass_classifier.predict(test_image)
training_set.class_indices
if mass_result[0][0] >= 0.5:
    mass_prediction = 'No Finding'
else:
    mass_prediction = 'Nodule Detected'
print(mass_prediction)

#atelectasis test
"""train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)
training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/nodule_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
mass_classifier = Sequential()
mass_classifier = load_model('AtelectasisRemote.h5')
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/TestAtelectasisPhoto.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
mass_result = mass_classifier.predict(test_image)
training_set.class_indices
if mass_result[0][0] >= 0.5:
    mass_prediction = 'No Finding'
else:
    mass_prediction = 'Atelectasis Detected'
print(mass_prediction)

#effusion test
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)
training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/effusion_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
mass_classifier = Sequential()
mass_classifier = load_model('EffusionRemote.h5')
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/TestEffusionPhoto.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
mass_result = mass_classifier.predict(test_image)
training_set.class_indices
if mass_result[0][0] >= 0.5:
    mass_prediction = 'No Finding'
else:
    mass_prediction = 'Effusion Detected'
print(mass_prediction)

#infiltration test
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range= 0.2,
    zoom_range= 0.2,
    horizontal_flip=True)
training_set  =train_datagen.flow_from_directory(
    'C:/Users/1439208/CNNTest/dataset/infiltration_training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
mass_classifier = Sequential()
mass_classifier = load_model('InfiltrationRemote.h5')
test_image = image.load_img('C:/Users/1439208/CNNTest/TestPhotos/TestInfiltrationPhoto.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
mass_result = mass_classifier.predict(test_image)
training_set.class_indices
if mass_result[0][0] >= 0.5:
    mass_prediction = 'No Finding'
else:
    mass_prediction = 'Infiltration Detected'
print(mass_prediction)"""