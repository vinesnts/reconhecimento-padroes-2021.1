import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit, train_test_split
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score

from utils import load_data


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

    @staticmethod
    def missing_cols(data):
        missing = set()
        for row in data:
            for k, v in enumerate(row):
                if np.isnan(v):
                    missing.add(k)
        return list(missing)

    @staticmethod
    def missing_cols_avg(missing_cols, data):
        missing_cols_dict = {}
        for col in missing_cols:
            values = np.array([])
            for row in data:
                if not np.isnan(row[col]):
                    values = np.append(values, row[col])
            missing_cols_dict[col] = np.average(values if len(values) > 0 else [0])
        return missing_cols_dict

    def fill_missing(self, data):
        missing_cols = KNeighborsKFoldClassifier.missing_cols(data)
        missing_cols_avg = KNeighborsKFoldClassifier.missing_cols_avg(missing_cols, data)
        for i, row in enumerate(data):
            new_row = np.copy(row)
            for k, v in enumerate(row):
                if np.isnan(v):
                    new_row[k] = missing_cols_avg[k]
            data[i] = new_row
        return data

    def classify(self, k_neighbors=1, test_size=.5, n_splits=100):
        sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size)

        self.acertos = np.array([])
        for train_index, test_index in sss.split(self.X, self.y):
            X_train, X_test = self.X[train_index], self.X[test_index]
            y_train, y_test = self.y[train_index], self.y[test_index]
            X_train = self.fill_missing(X_train) # <----- letra a
            X_test = self.fill_missing(X_test) # <----- letra b
            knn = KNeighborsClassifier(n_neighbors=k_neighbors, weights="distance", metric="euclidean")
            knn.fit(X_train, y_train.astype(float))

            acertos = knn.score(X_test, y_test)
            self.acertos = np.append(self.acertos, acertos)

    def intervalo_confianca(self):
        media = np.average(self.acertos)
        desvio = self.acertos.std()
        intervalo_confianca = (media-(1.96*desvio), media+(1.96*desvio))
        return intervalo_confianca


def main():
    data, _ = load_data('./data/processed.hungarian.csv', sep=',')
    X = np.array([tuple([int(x) if str(x).isnumeric() else np.NaN for x in list(row.values())[:13]]) for row in data])
    y = np.ravel([int(row['num']) for row in data])
    knn_kfold = KNeighborsKFoldClassifier(X, y)
    knn_kfold.classify(test_size=.1)
    print(knn_kfold.intervalo_confianca())


if __name__ == '__main__':
    main()