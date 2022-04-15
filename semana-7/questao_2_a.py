import numpy as np

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn_extra.cluster import KMedoids

from utils import load_data

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
        y_predicted = kmedoids.fit_predict(X_train)
        print(f'''
- {k}:
    - `{y_predicted}`
''')