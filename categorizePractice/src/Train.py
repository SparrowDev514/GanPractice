import numpy as np
from keras import layers, models
from keras.utils import np_utils
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

categories = ["0", "1", "2"]
nb_classes = len(categories)

f = np.load("categorizePractice/myDataSets/mydatasets.npz")
X_train, Y_train = f['x_train'], f['y_train']
X_test, Y_test = f['x_test'], f['y_test']
f.close()

x_train = X_train.astype("float") / 255
x_test = X_test.astype("float") / 255
y_train = np_utils.to_categorical(Y_train, nb_classes)
y_test = np_utils.to_categorical(Y_test, nb_classes)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(128, 128, 3)))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.MaxPool2D((2, 2)))
model.add(layers.Dropout(0.5))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dropout(0.25))
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dropout(0.25))
model.add(layers.Dense(nb_classes, activation="softmax"))
model.summary()

json_string = model.to_json()
open("categorizePractice/myDataSets/train.json", "w").write(json_string)

model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=["acc"])

model.fit(x_train, y_train, epochs=8, batch_size=256, validation_data=(x_test, y_test))

model.save_weights("categorizePractice/myDataSets/train.hdf5")

score = model.evaluate(x_test, y_test, verbose=0)
print("test loss : ", score[0])
print("test acc : ", score[1])
