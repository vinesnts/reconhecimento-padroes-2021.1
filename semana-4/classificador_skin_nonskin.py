import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support as score

X = []
y = []
with open('./Skin_NonSkin.csv', 'r') as file:
    for row in file.readlines():
        row_list = row.rstrip('\n').split('\t')
        X.append([int(x) for x in row_list[0:3]])
        y.append([int(x) for x in row_list[3]])
X = np.array(X)
y = np.ravel(y)

skf = StratifiedKFold(n_splits=100)
n_splits = skf.get_n_splits(X, y)
print(f'Número de splits: {n_splits}')

f_metrics_1 = np.array([])
f_metrics_2 = np.array([])
desvio_padrao = np.array([])
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
    knn.fit(X_train, y_train)
    
    predicts = knn.predict(X_test)
    _, _, f_metric, _ = score(y_test, predicts)
    f_metrics_1 = np.append(f_metrics_1,f_metric[0])
    f_metrics_2 = np.append(f_metrics_2,f_metric[1])

media_mf_1 = np.average(f_metrics_1)
max_mf_1 = f_metrics_1.max()
min_mf_1 = f_metrics_1.min()
media_mf_2 = np.average(f_metrics_2)
max_mf_2 = f_metrics_2.max()
min_mf_2 = f_metrics_2.min()
print(f'Média da medida-F classe 1: {round(media_mf_1, 3)}')
print(f'Máx. da medida-F classe 1: {round(max_mf_1, 3)}')
print(f'Mín. da medida-F classe 1: {round(min_mf_1, 3)}')
print(f'Média da medida-F classe 2: {round(media_mf_2, 3)}')
print(f'Máx. da medida-F classe 2: {round(max_mf_2, 3)}')
print(f'Mín. da medida-F classe 2: {round(min_mf_2, 3)}')

# plt.hist(f_metrics_1, bins=20)
# plt.savefig('f_metrics_1.png')

# plt.hist(f_metrics_2, bins=20)
# plt.savefig('f_metrics_2.png')

desvio_1 = f_metrics_1.std()
desvio_2 = f_metrics_2.std()
print(f'Desvio padrão classe 1: {desvio_1}')
print(f'Desvio padrão classe 2: {desvio_2}')

padrao_1 = (f_metrics_1 - media_mf_1) / desvio_1
print(f'''Intevalo de confiança classe 1: [{
    round(media_mf_1-(1.96*desvio_1), 3)}, {round(media_mf_1+(1.96*desvio_1), 3)}]''')

padrao_2 = (f_metrics_2 - media_mf_2) / desvio_2
print(f'''Intevalo de confiança classe 2: [{
    round(media_mf_2-(1.96*desvio_2), 3)}, {round(media_mf_2+(1.96*desvio_2), 3)}]''')