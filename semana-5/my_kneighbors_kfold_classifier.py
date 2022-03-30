import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score


class KNeighborsKFoldClassifier():

    def __init__(self, X, y, n_neighbors=1):
        self.X = X
        self.y = y
        self.n_neightbors = n_neighbors

    def load_data(self, filename):
        self.X = []
        self.y = []
        with open(filename, 'r') as file:
            for row in file.readlines():
                row_list = row.rstrip('\n').split(',')
                self.X.append([float(x) for x in row_list[:4]])
                self.y.append(row_list[4])
        self.X = np.array(self.X)
        self.y = np.ravel(self.y)

    def classify(self):
        self.accuracy_score = np.array([])
        for i in range(100):
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=.5)
            knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
            knn.fit(X_train, y_train)

            predicts = knn.predict(X_test)
            accuracy = accuracy_score(y_test, predicts)
            self.accuracy_score = np.append(self.accuracy_score, accuracy)

    def intervalo_confianca(self):
        media = np.average(self.accuracy_score)
        desvio = self.accuracy_score.std()
        intervalo_confianca = (media-(1.96*desvio), media+(1.96*desvio))
        return intervalo_confianca

