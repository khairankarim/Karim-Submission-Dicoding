# =====================================================================================
# PROBLEM A2
#
# Build a Neural Network Model for Horse or Human Dataset.
# The test will expect it to classify binary classes.
# Your input layer should accept 150x150 with 3 bytes color as the input shape.
# Don't use lambda layers in your model.
#
# The dataset used in this problem is created by Laurence Moroney (laurencemoroney.com).
#
# Desired accuracy and validation_accuracy > 83%
# ======================================================================================

import urllib.request
import zipfile
import tensorflow as tf
import os
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop


def solution_A2():
    data_url_1 = 'https://github.com/dicodingacademy/assets/releases/download/release-horse-or-human/horse-or-human.zip'
    urllib.request.urlretrieve(data_url_1, 'horse-or-human.zip')
    local_file = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/horse-or-human')

    data_url_2 = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/validation-horse-or-human.zip'
    urllib.request.urlretrieve(data_url_2, 'validation-horse-or-human.zip')
    local_file = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/validation-horse-or-human')
    zip_ref.close()

    TRAINING_DIR = 'data/horse-or-human'
    VALIDATION_DIR = 'data/validation-horse-or-human'
    train_datagen = ImageDataGenerator(
        rescale = 1.0/255.
    )

        # YOUR CODE HERE)

    # YOUR IMAGE SIZE SHOULD BE 150x150
    train_generator= train_datagen.flow_from_directory(TRAINING_DIR,
                                                    batch_size=20,
                                                    class_mode='binary',
                                                    target_size=(150, 150))
                                                    # YOUR CODE HERE

    test_datagen  = ImageDataGenerator( rescale = 1.0/255. )
    validation_generator =  test_datagen.flow_from_directory(VALIDATION_DIR,
                                                            batch_size=20,
                                                            class_mode  = 'binary',
                                                            target_size = (150, 150))

    model = tf.keras.models.Sequential([
        # YOUR CODE HERE, end with a Neuron Dense, activated by sigmoid
        tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(), 
        tf.keras.layers.Dense(512, activation='relu'), 
        tf.keras.layers.Dense(1, activation='sigmoid')
        ])
    
    model.summary()

    model.compile(optimizer=RMSprop(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
    
    history = model.fit(train_generator,
                              validation_data=validation_generator,
                              steps_per_epoch=10,
                              epochs=25,
                              validation_steps=8,
                              verbose=2)

    #-----------------------------------------------------------
    # Retrieve a list of list results on training and test data
    # sets for each training epoch
    #-----------------------------------------------------------
    # acc      = history.history[     'accuracy' ]
    # val_acc  = history.history[ 'val_accuracy' ]
    # loss     = history.history[    'loss' ]
    # val_loss = history.history['val_loss' ]

    # # epochs   = range(len(acc)) # Get number of epochs

    # #------------------------------------------------
    # # Plot training and validation accuracy per epoch
    # #------------------------------------------------
    # import matplotlib as plt
    # plt.plot  ( epochs,     acc, label='Training')
    # plt.plot  ( epochs, val_acc, label='Validation')
    # plt.title ('Training and validation accuracy')
    # plt.legend()
    # plt.figure()

    # #------------------------------------------------
    # # Plot training and validation loss per epoch
    # #------------------------------------------------
    # plt.plot  ( epochs,     loss, label='Training')
    # plt.plot  ( epochs, val_loss, label='Validation')
    # plt.legend()
    # plt.title ('Training and validation loss')
    
    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model=solution_A2()
    model.save("model_A2.h5")
