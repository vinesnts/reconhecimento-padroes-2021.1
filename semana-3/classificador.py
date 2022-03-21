import numpy as np

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score

TEST_RATE = 0.3

CLASSE1 = "1"
CLASSE2 = "2"
CLASSE3 = "3"

class WineClassifier():

    def __init__(self) -> None:
        self.load_wine()
        self.train_data()
        self.calcular_matriz_confusao()

    def load_wine(self):
        self.wine_classes = []
        self.wine_data = []
        with open('./wine.csv', 'r') as file:
            for row in file.readlines():
                row_list = row.rstrip('\n').split(',')
                self.wine_data.append(row_list[1:14])
                self.wine_classes.append(row_list[0])

    def train_data(self, n_neighbors=1):
        self.x_treino, self.x_teste, self.y_treino, self.y_teste = train_test_split(self.wine_data, list(self.wine_classes), test_size=TEST_RATE)
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors, weights="distance", metric="euclidean")
        self.knn.fit(self.x_treino, self.y_treino)

    def calcular_matriz_confusao(self):

        predicts = self.knn.predict(self.x_teste)
        self.matriz_confusao = confusion_matrix(self.y_teste, predicts)

    def taxa_acerto(self):
        print(f'Taxa de acerto: {round(self.knn.score(self.x_teste, self.y_teste) * 100, 2)}%')

    def imprimir_matriz_confusao(self):
        classes = (CLASSE1, CLASSE2, CLASSE3)
        print(classes)
        for i, row in enumerate(self.matriz_confusao):
            print(classes[i], tuple(row))

    def metrics(self):
        predicts = self.knn.predict(self.x_teste)
        return score(self.y_teste, predicts)

    def acertos(self):
        return self.knn.score(self.x_teste, self.y_teste)

print('1 - Resultados Wine 1NN, usando distância de Euclidiana')

wine = WineClassifier()

print('-------------------------------------------------------')

print('Matriz de confusão: ')
wine.imprimir_matriz_confusao()

print('-------------------------------------------------------')

precision, recall, fscore, support = wine.metrics()
print((CLASSE1, CLASSE2, CLASSE3))
print(f'Precisão: {precision}')
print(f'Recall: {recall}')
print(f'Métrica-F: {fscore}')
print(f'Taxa VN: {support}')
print(f'Acertos: {wine.acertos()}')
# print(f'Recall classe 1: {round(recall_classe1 * 100, 2)}%')
# recall_classe2 = wine.recall(CLASSE2)
# print(f'Recall classe 2: {round(recall_classe2 * 100, 2)}%')
# recall_classe3 = wine.recall(CLASSE3)
# print(f'Recall classe 3: {round(recall_classe3 * 100, 2)}%')
