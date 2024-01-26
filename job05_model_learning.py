import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

X_train, X_test, Y_train, Y_test = np.load('./shopping_data_max_29_wordsize_6482.npy',allow_pickle=True)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

model = Sequential()
model.add(Embedding(6482,300,input_length=29))                     #벡터화하여 의미를 만들어준다 input_dim = 차원의 수를 대입,output_dim = 차원수를 축소
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))         #1차원으로 겹쳐서 덩어리를 만든다
model.add(MaxPooling1D(pool_size=1))                                                    #poolsize 1이라 1개만
model.add(LSTM(128, activation='tanh', return_sequences=True))                      #return_sequences true면 여러개를 이어서 출력 false면 마지막만 출력
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=128, epochs=10, validation_data=(X_test, Y_test))
model.save('./models/news_category_classification_model_{}.h5'.format(fit_hist.history['val_accuracy'][-1]))
plt.plot(fit_hist.history['val_accuracy'], label = 'validation accuracy')
plt.plot(fit_hist.history['accuracy'], label = 'accuracy')
plt.legend()
plt.show()