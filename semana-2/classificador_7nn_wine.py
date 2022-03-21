from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

wine = datasets.load_wine()

treino1Data = wine.data[:30]
treino1Target = wine.target[:30]
treino2Data = wine.data[60:95]
treino2Target = wine.target[60:95]
treino3Data = wine.data[130:154]
treino3Target = wine.target[130:154]
treinoData = np.concatenate((treino1Data, treino2Data, treino3Data))
treinoTarget = np.concatenate((treino1Target, treino2Target, treino3Target))

teste1Data = wine.data[30:59]
teste1Target = wine.target[30:59]
teste2Data = wine.data[95:130]
teste2Target = wine.target[95:130]
teste3Data = wine.data[154:178]
teste3Target = wine.target[154:178]
testeData = np.concatenate((teste1Data, teste2Data, teste3Data))
testeTarget = np.concatenate((teste1Target, teste2Target, teste3Target))

knn = KNeighborsClassifier(n_neighbors=7, weights="distance", metric="euclidean")
knn.fit(treinoData, treinoTarget)

print(knn.predict(testeData))
print(knn.score(testeData, testeTarget))