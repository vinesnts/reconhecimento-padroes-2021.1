import matplotlib.pyplot as plt
import random
import numpy as np

from math import sqrt
from utils import load_data

UNDEFINED = (99999, None)

def distancia_euclidiana(treino, teste):
    soma = 0
    if len(treino) == len(teste):
        for i in range(len(treino) - 1):
            soma += ((float(treino[i]) - float(teste[i])) ** 2)
            
    return sqrt(soma)

class KMedias():

    def __init__(self, X: list, k: int, i: int = 10,) -> None:
        self.X= X
        self.i = i

        self.k = k
        self.n_columns = len(self.X[0]) if self.X else 0

    def gen_random_centroids(self) -> None:
        self.centroids = []
        for _ in range(self.k):
            self.centroids.append([random.uniform(0,10) for _ in range(self.n_columns)])

    def gen_undefined_out(self) -> list:
        return [UNDEFINED for _ in range(len(self.X))]

    def update_centroids(self):
        groups = [[] for _ in range(self.k)]
        for y, x in zip(self.y_predict, self.X):
            for i in range(self.k):
                if y[1] == i:
                    groups[i].append(x)

        for i_group, group in enumerate(groups):
            for i_col, _ in enumerate(group[0] if group else []):
                col_values = [next(v for i, v in enumerate(row) if i == i_col) for row in group]
                self.centroids[i_group][i_col] = np.average(np.array(col_values))

    def predict(self, init: list = None) -> list:
        centroid = None
        self.y_predict = self.gen_undefined_out()

        if init:
            self.centroids = init
        else:
            self.gen_random_centroids()

        for _ in range(self.i):
            new_group = True
            while (new_group):
                new_group = False
                for i_x, x in enumerate(self.X):
                    min = UNDEFINED
                    for i_centroid, centroid in enumerate(self.centroids):
                        distance = distancia_euclidiana(x, centroid)
                        if distance < min[0]:
                            min = (distance, i_centroid)
                    if self.y_predict[i_x] != min:
                        new_group = True
                        self.y_predict[i_x] = min

            self.update_centroids()

        return [group for distance, group in self.y_predict]


data, _ = load_data('./data/iris.csv', sep=',')
X = [[float(v) for k,v in row.items() if k != 'class'] for row in data]
y_real = [next(v for k,v in row.items() if k == 'class') for row in data]

kmedias = KMedias(X, 9, 10)
print(kmedias.predict(init=None))

init = [[2.352862170473257, 7.380137817184172, 7.908954123534768, 8.340724805064577], [5.6822970518803615, 9.230052999390043, 1.1737175429575752, 1.4521459751119448], [7.115591366393178, 9.852234778730818, 8.90078446861468, 5.541565009366871]]

clusters = [3, 6, 9]
for k in clusters:
    kmeans = KMedias(X=X, k=k, i=10)

    y_predicted = kmeans.predict(init=init if k == 3 else None)
    centroids = kmeans.centroids
    groups = {i:[] for i, _ in enumerate(centroids)}
    for centroid_i, _ in enumerate(centroids):
        for y_index, y in enumerate(y_predicted):
            if centroid_i == y:
                groups[centroid_i].append(y_real[y_index])

    for k_group, group in groups.items():
        group = np.array(group)
        unique, counts = np.unique(group, return_counts=True)

        setosa = None
        virginica = None
        versicolor = None
        for i, v in enumerate(unique):
            if v == 'setosa':
                setosa = counts[i]
            if v == 'virginica':
                virginica = counts[i]
            if v == 'versicolor':
                versicolor = counts[i]

        classes = ['setosa', 'virginica', 'versicolor']
        fig = plt.figure(figsize=(10,5))

        plt.bar(classes, [
            setosa if setosa else 0,
            virginica if virginica else 0,
            versicolor if versicolor else 0
        ], width=0.4)
        plt.xlabel('Classes')
        plt.ylabel('Nº de ocorrências')
        plt.title(f'K: {k}, group: {k_group}')
        plt.savefig(f'saida/questao_1_c_k-{k}_group-{k_group}.png')
