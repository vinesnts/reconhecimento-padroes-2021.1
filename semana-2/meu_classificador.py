from math import sqrt
import pandas as pd

class ClassificadorVizinho():

    @classmethod
    def createIrisList(self):
        irisList = []
        for i in range(150):
            irisIndex = []
            data = pd.read_csv('./iris.csv', skiprows=i + 1, nrows=1)
            
            for row in enumerate(data):
                irisIndex.append(row[1])


            irisList.append(irisIndex)

        return irisList

    @classmethod
    def distanciaEuclidiana(self, treino, teste):
        soma = 0
        if len(treino) == len(teste):
            for i in range(len(treino) - 1):
                soma += ((float(treino[i]) - float(teste[i])) ** 2)
                

        return sqrt(soma)

    @classmethod
    def distanciaMinkowski(self, treino, teste, p):
        soma = 0
        if len(treino) == len(teste):
            for i in range(len(treino) - 1):
                soma += ( abs(float(treino[i]) - float(teste[i])) ** p)
                

        return soma ** (1/p)

    @classmethod
    def calcularDistancias(self, treino, teste, tipoDistancia = 'e', p = 1):
        distancias = []
        for te in teste:
            distanciasExemplo = []
            for tr in treino:
                if tipoDistancia == 'e':
                    distancia = self.distanciaEuclidiana(tr, te)
                elif tipoDistancia == 'm':
                    distancia = self.distanciaMinkowski(tr, te, p)
                distanciasExemplo.append((tr[4], distancia))

            distancias.append(distanciasExemplo)

        return distancias

    def get1NN(distancias):
        menores = []
        for distanciasExemplo in distancias:
            menor = ('indefinido', 999999)
            for v in distanciasExemplo:
                if v[1] < menor[1]:
                    menor = v

            menores.append(menor)

        return menores

    def get7NN(distancias):
        menores = []
        for distanciasExemplo in distancias:
            nClasse = []
            for u in range(7):
                menor = ('indefinido', 9999999)
                if len(nClasse) < 7:
                    for v in distanciasExemplo:
                        if v[1] < menor[1] and v not in nClasse:
                            menor = v

                    nClasse.append(menor)

            menores.append(nClasse)
            nClasse = []

        return menores

    def contarMaioriaKNN(seteMenores):
        somaMaioria = []
        for sM in seteMenores:
            classes = {}
            for m in sM:
                if m[0] in classes:
                    classes[m[0]] += 1
                else:
                    classes[m[0]] = 1

            somaMaioria.append(classes)
            classes = {}

        return somaMaioria

    def contarPesosKNN(seteMenores):
        somaMaioria = []
        for sM in seteMenores:
            classes = {}
            for m in sM:
                if m[0] in classes:
                    classes[m[0]] += 1/float(m[1] + 0.0000001)
                else:
                    classes[m[0]] = 1/float(m[1] + 0.0000001)

            somaMaioria.append(classes)
            classes = {}

        return somaMaioria

 
        
iris = ClassificadorVizinho.createIrisList()

treino = iris[:25] + iris[50:75] + iris[100:125]
teste = iris[25:50] + iris[75:100] + iris[125:150]

print('1 - Resultados Iris 1NN, usando distância de Euclidiana')
distancias = ClassificadorVizinho.calcularDistancias(treino, teste)
menores = ClassificadorVizinho.get1NN(distancias)

acertos = 0
erros = 0
for i in menores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(menores[:25])}")

acertos = 0
erros = 0
for i in menores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(menores[25:50])}")

acertos = 0
erros = 0
for i in menores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(menores[50:75])}")

print('---------------------------------------------------')
print('2 - Resultados Iris 1NN, usando distância de Minkowski com p = 1')
distancias = ClassificadorVizinho.calcularDistancias(treino, teste, 'm', 1)
menores = ClassificadorVizinho.get1NN(distancias)

acertos = 0
erros = 0
for i in menores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(menores[:25])}")

acertos = 0
erros = 0
for i in menores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(menores[25:50])}")

acertos = 0
erros = 0
for i in menores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(menores[50:75])}")

print('---------------------------------------------------')
print('2 - Resultados Iris 1NN, usando distância de Minkowski com p = 2')
distancias = ClassificadorVizinho.calcularDistancias(treino, teste, 'm', 2)
menores = ClassificadorVizinho.get1NN(distancias)

acertos = 0
erros = 0
for i in menores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(menores[:25])}")

acertos = 0
erros = 0
for i in menores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(menores[25:50])}")

acertos = 0
erros = 0
for i in menores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(menores[50:75])}")

print('---------------------------------------------------')
print('2 - Resultados Iris 1NN, usando distância de Minkowski com p = 4')
distancias = ClassificadorVizinho.calcularDistancias(treino, teste, 'm', 4)
menores = ClassificadorVizinho.get1NN(distancias)

acertos = 0
erros = 0
for i in menores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(menores[:25])}")

acertos = 0
erros = 0
for i in menores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(menores[25:50])}")

acertos = 0
erros = 0
for i in menores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(menores[50:75])}")


print('---------------------------------------------------')
print('3.b - Resultados Iris 7NN, usando distância de Euclidiana sem peso')

seteMenores = ClassificadorVizinho.get7NN(distancias)
somaMaioria = ClassificadorVizinho.contarMaioriaKNN(seteMenores)

maiores = []
for i in somaMaioria:
    maior = ('indefinido', 0)
    # print(i)
    for j in i.items():
        if j[1] > maior[1]:
            maior = (j[0], j[1])

    maiores.append(maior)

acertos = 0
erros = 0
for i in maiores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(maiores[:25])}")

acertos = 0
erros = 0
for i in maiores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(maiores[25:50])}")

acertos = 0
erros = 0
for i in maiores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(maiores[50:75])}")


seteMenores = ClassificadorVizinho.get7NN(distancias)
somaMaioria = ClassificadorVizinho.contarPesosKNN(seteMenores)

# pesos = ClassificadorVizinho.contarPesosKNN(seteMenores)
# for i in pesos:
#     print(i)

print('---------------------------------------------------')
print('3.a - Resultados Iris 7NN, usando distância de Euclidiana com peso')
maiores = []
for i in somaMaioria:
    maior = ('indefinido', 0)
    # print(i)
    for j in i.items():
        if j[1] > maior[1]:
            maior = (j[0], j[1])

    maiores.append(maior)

acertos = 0
erros = 0
for i in maiores[:25]:
    if i[0] == 'Iris-setosa':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de setosa: {(acertos * 100) / len(maiores[:25])}")

acertos = 0
erros = 0
for i in maiores[25:50]:
    if i[0] == 'Iris-versicolor':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de versicolor: {(acertos * 100) / len(maiores[25:50])}")

acertos = 0
erros = 0
for i in maiores[50:75]:
    if i[0] == 'Iris-virginica':
        acertos += 1
    else:
        erros += 1

print(f"Acertos de virginica: {(acertos * 100) / len(maiores[50:75])}")







