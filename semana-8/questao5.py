import numpy as np

from PIL import Image
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors

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

n_class = 40
n_sample = 10
X, y = load_images(n_class, n_sample)

sss = StratifiedShuffleSplit(test_size=.5, n_splits=10)
images = []
images_neighbor = []
for train_index, test_index in sss.split(X,y):
  images_split = []
  images_neighbor_split = []
  X_train, X_test = X[train_index], X[test_index]
  y_train, y_test = y[train_index], y[test_index]

  knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
  knn.fit(X_train, y_train)

  predicts = knn.predict(X_test)
  
  for i, predict in enumerate(predicts):
    couple = []
    if predict != y_test[i]:
      neighbor = knn.kneighbors([X_test[i]], n_neighbors=1, return_distance=False)
      image_matrix = np.array_split(X_test[i], 112)
      neighbor_matrix = np.array_split(X_train[neighbor[0][0]], 112)
      couple.append(image_matrix)
      couple.append(neighbor_matrix)
    if couple:
      images_split.append(couple)
  images.append(images_split)


for i, images_split in enumerate(images):
  images1 = [np.concatenate(image, axis=1) for image in images_split]
  Image.fromarray(np.concatenate(np.array(images1))).save(f'./static/questao5_split_{i+1}.png')
  print(f'- Split {i+1}: ![Questão 5 split {i+1}](static/questao5_split_{i+1}.png)')