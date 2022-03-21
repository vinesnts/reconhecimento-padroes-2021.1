import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import precision_recall_fscore_support as score

X = []
y = []
with open('./wine.csv', 'r') as file:
    for row in file.readlines():
        row_list = row.rstrip('\n').split(',')
        X.append([float(x) for x in row_list[1:14]])
        y.append([float(x) for x in row_list[0]])
X = np.array(X)
y = np.ravel(y)


acertos = {x: np.array([]) for x in range(1,16)}
for i in range(1, 16):
    for j in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
        knn = KNeighborsClassifier(n_neighbors=i, weights="distance", metric="euclidean")
        knn.fit(X_train, y_train)

        predicts = knn.predict(X_test)
        acerto = knn.score(X_test, y_test)
        acertos[i] = np.append(acertos[i], acerto)

for i in range(1,16):
    media = np.average(acertos[i])
    desvio = acertos[i].std()
    intervalo_confianca = (media-(1.96*desvio), media+(1.96*desvio))
    print(f'Média de acertos wine {i}NN: {round(media, 3)}')
    print(f'Desvio padrão de acertos wine {i}NN: {round(desvio, 3)}')
    print(f'''Intervalo de confiança acertos wine {i}NN: [{
        round(intervalo_confianca[0], 3)}, {round(intervalo_confianca[1], 3)}]''')