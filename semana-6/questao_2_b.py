import numpy as np
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers.core import Dense

from non_binary_categorizer import NonBinaryConverter
from utils import load_data

data, columns = load_data('./data/wine.csv', ',')
nb_converter = NonBinaryConverter(data, ['class'])
data, columns = nb_converter.convert_data(), nb_converter.generate_columns()

X = [[float(v) for k, v in row.items() if 'class' not in k] for row in data]
y = [[int(v) for k, v in row.items() if 'class' in k] for row in data]

acuracias = np.array([])
for i in range(30):
  X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)

  model = Sequential()
  model.add(Dense(26, input_dim=13))
  model.add(Dense(3, activation="softmax"))
  model.compile(loss="categorical_crossentropy", metrics=['accuracy'])
  model.fit(X_train, y_train, epochs=100, batch_size=1)

  _, accuracy = model.evaluate(X_test, y_test)
  print(accuracy)
  acuracias = np.append(acuracias, accuracy)

print(f'Desvio padrão: {acuracias.std()}')
print(f'Média: {np.average(acuracias)}')

# n_epocas = 1000
# clf = MLPClassifier(hidden_layer_sizes=(178) ,activation="logistic", solver="adam", max_iter=n_epocas)
# clf.fit(X_train, y_train)

# acertos = 0
# for i, v in enumerate(y_test):
#   if clf.predict(X_test)[i] == v:
#     acertos += 1

# print(acertos / len(X_test))
