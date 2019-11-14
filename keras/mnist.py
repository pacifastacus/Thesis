import numpy as np
from keras import models, layers
from keras.utils import to_categorical
from keras import datasets
import pickle

#Load the MNIST dataset and convert the datas
trainSet, testSet = datasets.mnist.load_data('mnist.npz')
#flatten images to vectors
train_d = trainSet[0].reshape(trainSet[0].shape[0],trainSet[0].shape[1]*trainSet[0].shape[2])
test_d = testSet[0].reshape(testSet[0].shape[0],testSet[0].shape[1]*testSet[0].shape[2])
#normalize pixel values
#train_d = train_d.astype('float32') / 255
#test_d = test_d.astype('float32') / 255
#convert labels to one-hot
train_l = to_categorical(trainSet[1])
test_l = to_categorical(testSet[1])

#Building network
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(loss = 'categorical_crossentropy',
    optimizer = 'rmsprop',
    metrics = ['acc'])

#Train network
history = network.fit(train_d,
                    train_l,
                    epochs=20,
                    batch_size=512)

#Write out history to file
with open('history.bin', mode='wb') as f:
    pickle.dump(history, f, pickle.HIGHEST_PROTOCOL)
    
