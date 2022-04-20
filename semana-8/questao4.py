import numpy as np

from PIL import Image
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier

def load_images(n_class: int, n_sample: int) -> list[list]:
  X = []
  y = []
  for i in range(1, n_class + 1):
    images = []
    for j in range(1, n_sample + 1):
      image = Image.open(f'./static/orl/class_{str(i).rjust(2, "0")}/sample_{str(j).rjust(2, "0")}.png')
      image_matrix = np.asarray(image)
      image_list = []
      for row in image_matrix:
        for value in row:
          image_list.append(value)
      X.append(image_list)
      y.append(i)

  return np.array(X), np.array(y)

n_class = 40
n_sample = 10
X, y = load_images(n_class, n_sample)

sss = StratifiedShuffleSplit(test_size=.5, n_splits=10)
acertos = []
for train_index, test_index in sss.split(X,y):
  X_train, X_test = X[train_index], X[test_index]
  y_train, y_test = y[train_index], y[test_index]

  knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
  knn.fit(X_train, y_train)

  acertos.append(knn.score(X_test, y_test))

[print(f'Taxa de acerto (classe {i+1}): {acerto}') for i, acerto in enumerate(acertos)]
print(f'Média de acertos total: {round(np.average(np.array(acertos)), 3)}')