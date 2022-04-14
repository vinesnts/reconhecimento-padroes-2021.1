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


clusters = [3, 6, 9]
medias = {
    3: [],
    6: [],
    9: []
}
desvios = {
    3: [],
    6: [],
    9: []
}
for k in clusters:
    centroids = None
    iterations = 10
    for i in range(iterations):
        kmeans = KMeans(
            n_clusters=k,
            n_init=1,
            max_iter=1,
            random_state=1,
            init=centroids if centroids is not None else 'k-means++'
        )
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_

        distancias = []
        for row in X:
            for centroid in kmeans.cluster_centers_:
                distancias.append(distancia_euclidiana(row, centroid))

        distancias = np.array(distancias)
        medias[k].append(round(np.average(distancias), 3))
        desvios[k].append(round(distancias.std(), 3))

print('>>>> Tabela de médias <<<<')
print('|i|3|6|9|')
print('|-|-|-|-|')
for index, _ in enumerate(medias[3]):
    print(f'| {index + 1} | {medias[3][index]} | {medias[6][index]} | {medias[9][index]} |')

print('>>>> Tabela de desvios <<<<')
print('|i|3|6|9|')
print('|-|-|-|-|')
for index, _ in enumerate(desvios[3]):
    print(f'| {index + 1} | {desvios[3][index]} | {desvios[6][index]} | {desvios[9][index]} |')
