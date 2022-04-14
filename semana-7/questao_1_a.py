import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from utils import load_data

from sklearn.cluster import KMeans

def distancia_euclidiana(treino, teste):
    soma = 0
    if len(treino) == len(teste):
        for i in range(len(treino) - 1):
            soma += ((float(treino[i]) - float(teste[i])) ** 2)
            

    return sqrt(soma)

data, _ = load_data('./data/iris.csv', sep=',')
X = np.array([[float(v) for k,v in row.items() if k != 'class'] for row in data])
y_real = np.array([next(v for k,v in row.items() if k == 'class') for row in data])


clusters = [3, 6, 9]
for k in clusters:
    kmeans = KMeans(
        n_clusters=k,
        n_init=1,
        max_iter=10,
        random_state=1,
    )

    y_predicted = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_
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
        plt.savefig(f'questao_1_a_k-{k}_group-{k_group}.png')
