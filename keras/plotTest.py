#!/usr/bin/env python3
#from keras import models, layers
import matplotlib.pyplot as plot
import numpy as np
import pickle

with open('history.bin', mode='rb') as f:
	history = pickle.load(f)

x = history.epoch + np.ones(len(history.epoch))
y = np.arange(0,1,0.05) + 0.05
loss = history.history.get('loss')
acc = history.history.get('acc')

plot.plot(x, loss, label="loss")
plot.plot(x, acc, label="accuracy")
plot.xticks(x)
plot.yticks(y)
plot.grid()
plot.legend()
plot.show()