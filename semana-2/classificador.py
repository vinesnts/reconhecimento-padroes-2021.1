from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = datasets.load_iris()

treinoSetData = iris.data[:25]
treinoSetTarget = iris.target[:25]
treinoVerData = iris.data[50:75]
treinoVerTarget = iris.target[50:75]
treinoVirData = iris.data[100:125]
treinoVirTarget = iris.target[100:125]
treinoData = np.concatenate((treinoSetData, treinoVerData, treinoVirData))
treinoTarget = np.concatenate((treinoSetTarget, treinoVerTarget, treinoVirTarget))

testeSetData = iris.data[25:50]
testeSetTarget = iris.target[25:50]
testeVerData = iris.data[75:100]
testeVerTarget = iris.target[75:100]
testeVirData = iris.data[125:150]
testeVirTarget = iris.target[125:150]
testeData = np.concatenate((testeSetData, testeVerData, testeVirData))
testeTarget = np.concatenate((testeSetTarget, testeVerTarget, testeVirTarget))

knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
knn.fit(treinoData, treinoTarget)

print(knn.predict(testeData))
print(knn.score(testeData, testeTarget))