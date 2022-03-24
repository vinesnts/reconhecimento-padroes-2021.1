import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support as score

X = []
y = []
with open('./iris.csv', 'r') as file:
    for row in file.readlines():
        row_list = row.rstrip('\n').split(',')
        X.append([float(x) for x in row_list[:4]])
        y.append(row_list[4])
X = np.array(X)
y = np.ravel(y)

acertos = np.array([])
acertos_1 = np.array([])
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
    knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
    knn.fit(X_train, y_train)
    
    X_train_1 = np.array([x[:2] for x in X_train])
    X_test_1 = np.array([x[:2] for x in X_test])
    knn_1 = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
    knn_1.fit(X_train_1, y_train)

    predicts = knn.predict(X_test)
    acerto = knn.score(X_test, y_test)
    acertos = np.append(acertos, acerto)

    predicts_1 = knn_1.predict(X_test_1)
    acerto_1 = knn_1.score(X_test_1, y_test)
    acertos_1 = np.append(acertos_1, acerto_1)

print(f'Diferenças: {acertos - acertos_1}')
diferencas = acertos - acertos_1
media_dif = np.average(diferencas)
desvio_dif = diferencas.std()
intervalo_confianca_dif = (media_dif-(1.96*desvio_dif), media_dif+(1.96*desvio_dif))
print(f'Média das diferenças: {round(media_dif, 3)}')
print(f'Desvio padrão das diferenças: {round(desvio_dif, 3)}')
print(f'''Intervalo de confiança: [{
    round(intervalo_confianca_dif[0], 3)}, {round(intervalo_confianca_dif[1], 3)}]''')

media = np.average(acertos)
desvio = acertos.std()
intervalo_confianca = (media-(1.96*desvio), media+(1.96*desvio))
print(f'Média de acertos iris: {round(media, 3)}')
print(f'Desvio padrão de acertos iris: {round(desvio, 3)}')
print(f'''Intervalo de confiança acertos iris: [{
    round(intervalo_confianca[0], 3)}, {round(intervalo_confianca[1], 3)}]''')

media_1 = np.average(acertos_1)
desvio_1 = acertos.std()
intervalo_confianca_1 = (media_1-(1.96*desvio_1), media_1+(1.96*desvio_1))
print(f'Média de acertos iris sem última coluna: {round(media_1, 3)}')
print(f'Desvio padrão de acertos iris sem última coluna: {round(desvio_1, 3)}')
print(f'''Intervalo de confiança acertos iris sem última coluna: [{
    round(intervalo_confianca_1[0], 3)}, {round(intervalo_confianca_1[1], 3)}]''')