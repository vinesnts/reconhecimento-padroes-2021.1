import numpy as np

from my_kneighbors_kfold_classifier import KNeighborsKFoldClassifier
from utils import load_data

data, columns = load_data('./data/questao_1_c_export.csv')
X = np.array([tuple([int(x) for x in list(row.values())[:28]]) + tuple([int(x) for x in list(row.values())[29:46]]) for row in data])
y = np.ravel([int(row['G3']) for row in data])
knn_kfold = KNeighborsKFoldClassifier(X, y)
knn_kfold.classify()
print(f'Intervalo de confiança: {knn_kfold.intervalo_confianca()}')