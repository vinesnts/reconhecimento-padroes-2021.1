import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn_extra.cluster import KMedoids

from utils import load_data

def calc_taxa_acerto(acertos, erros, classe):
    return round((acertos[classe] / (acertos[classe] + erros[classe])) * 100, 3)

data, _ = load_data('./data/iris.csv', sep=',')
X = np.array([[float(v) for k,v in row.items() if k != 'class'] for row in data])
y = np.array([next(v for k,v in row.items() if k == 'class') for row in data])


sss = StratifiedShuffleSplit(test_size=.5, n_splits=1)
for train_index, test_index in sss.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clusters = [9, 18, 27, 45, 72]
    for k in clusters:
        kmedoids = KMedoids(
            n_clusters=k,
            max_iter=10,
            random_state=1
        )
        kmedoids.fit(X_train)
        centroids = kmedoids.cluster_centers_
        X_train_reduced = []
        y_train_reduced = []
        for i, row in enumerate(X_train):
            for centroid in centroids:
                equal = True
                for x_value, centroid_value in zip(row, centroid):
                    if x_value != centroid_value:
                        equal = False
                        break
                if equal:
                    X_train_reduced.append(row)
                    y_train_reduced.append(y_train[i])

        knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
        knn.fit(X_train_reduced, y_train_reduced)

        predicts = knn.predict(X_test)
        acertos = {
            'setosa': 0,
            'virginica': 0,
            'versicolor': 0
        }
        erros = {
            'setosa': 0,
            'virginica': 0,
            'versicolor': 0
        }
        for i, predict in enumerate(predicts):
            if y_test[i] == predict:
                acertos[predict] += 1
            else:
                erros[predict] += 1
        print(f'- K = {k}:')
        for classe in acertos:
            print(f' - Taxa de acerto {classe}: {calc_taxa_acerto(acertos,erros,classe)}')