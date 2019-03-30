# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:53:27 2019

@author: YASH SAINI
"""
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

filename = "mac.txt"

text =(open(filename).read()).lower()
U_char = sorted(list(set(text)))

chr_int={}
int_chr={}

index=0
for i in U_char:
    chr_int[i]=index
    int_chr[index]=i
    index+=1
    
X = []
Y = []

for i in range(0, len(text) - 50):
    sequence = text[i:i + 50]
    label =text[i + 50]
    X.append([chr_int[char] for char in sequence])
    Y.append(chr_int[label])

X_modified = np.reshape(X, (len(X), 50, 1))
X_modified = X_modified / float(len(unique_chars))
Y_modified = np_utils.to_categorical(Y)

# defining the LSTM model
model = Sequential()
model.add(LSTM(300, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2)) #to avoid overfitting
model.add(LSTM(300))
model.add(Dropout(0.2)) #to avoid overfitting
model.add(Dense(Y_modified.shape[1], activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam')

# fitting the model
model.fit(X_modified, Y_modified, epochs=1, batch_size=30)

# picking a random seed
start_index = np.random.randint(0, len(X)-1)
new_string = X[start_index]

# generating characters
for i in range(50):
    x = np.reshape(new_string, (1, len(new_string), 1))
    x = x / float(len(U_char))

    #predicting
    pred_index = np.argmax(model.predict(x, verbose=0))
    char_out = int_chr[pred_index]
    seq_in = [int_chr[value] for value in new_string]
    print(char_out)

    new_string.append(pred_index)
    new_string = new_string[1:len(new_string)]
    