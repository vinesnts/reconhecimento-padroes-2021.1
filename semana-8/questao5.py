import numpy as np

from PIL import Image
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier

def load_images(n_class: int, n_sample: int) -> list[list]:
  X = []
  y = []
  for i in range(1, n_class + 1):
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

def fill_missing(array):
  max_dim = [np.max([a.shape[0] for a in array]), np.max([a.shape[1] for a in array])]
  new_array = []
  for a in array:
      temp = np.zeros((max_dim[0], max_dim[1]))
      temp[:a.shape[0], :a.shape[1]] = a
      new_array.append(temp)
  return new_array

n_class = 40
n_sample = 10
X, y = load_images(n_class, n_sample)

sss = StratifiedShuffleSplit(test_size=.5, n_splits=10)
images = []
for train_index, test_index in sss.split(X,y):
  images_split = []
  X_train, X_test = X[train_index], X[test_index]
  y_train, y_test = y[train_index], y[test_index]

  knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
  knn.fit(X_train, y_train)

  predicts = knn.predict(X_test)
  
  for i, predict in enumerate(predicts):
    if predict != y_test[i]:
      image_matrix = np.array_split(X_test[i], 112)
      images_split.append(image_matrix)
  images.append(images_split)

images1 = [np.concatenate(image, axis=1) for image in images]
images1 = fill_missing(images1)
Image.fromarray(np.concatenate(np.array(images1))).show()