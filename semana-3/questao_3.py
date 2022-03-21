from sklearn.metrics import recall_score, precision_score, f1_score, confusion_matrix

from math import sqrt
import pandas as pd

CLASSE1 = '1'
CLASSE2 = '2'
CLASSE3 = '3'

def create_list():
    wine_list = []
    with open('./wine.csv', 'r') as file:
        for row in file.readlines():
            row_list = row.rstrip('\n').split(',')
            wine_list.append(row_list)
    return wine_list

def distancia_euclidiana(treino, teste):
    soma = 0
    if len(treino) == len(teste):
        for i in range(1, len(treino)):
            soma += ((float(treino[i]) - float(teste[i])) ** 2)
            

    return sqrt(soma)

def distancia_minkowski(treino, teste, p):
    soma = 0
    if len(treino) == len(teste):
        for i in range(len(treino) - 1):
            soma += ( abs(float(treino[i]) - float(teste[i])) ** p)
            

    return soma ** (1/p)

def calcular_distancias(treino, teste, tipoDistancia = 'e', p = 1):
    distancias = []
    for te in teste:
        distanciasExemplo = []
        for tr in treino:
            if tipoDistancia == 'e':
                distancia = distancia_euclidiana(tr, te)
            elif tipoDistancia == 'm':
                distancia = distancia_minkowski(tr, te, p)
            distanciasExemplo.append((tr[0], distancia))

        distancias.append(distanciasExemplo)

    return distancias

def get_1nn(distancias):
    menores = []
    for distanciasExemplo in distancias:
        menor = ('indefinido', 999999)
        for v in distanciasExemplo:
            if v[1] < menor[1]:
                menor = v

        menores.append(menor)

    return menores

def get_7nn(distancias):
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

def contar_maioria_knn(seteMenores):
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

def contar_pesos_knn(seteMenores):
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

def matriz_confusao():
    matriz_confusao = {
        CLASSE1: {CLASSE1: 0, CLASSE2: 0, CLASSE3: 0},
        CLASSE2: {CLASSE1: 0, CLASSE2: 0, CLASSE3: 0},
        CLASSE3: {CLASSE1: 0, CLASSE2: 0, CLASSE3: 0},
    }

    for i, value in enumerate(menores):
        if i < 18:
            if value[0] == CLASSE1:
                matriz_confusao[CLASSE1][CLASSE1] += 1
            else:
                matriz_confusao[CLASSE1][value[0]] += 1
        elif i >= 18 and i < 36:
            if value[0] == CLASSE2:
                matriz_confusao[CLASSE2][CLASSE2] += 1
            else:
                matriz_confusao[CLASSE2][value[0]] += 1
        elif i >= 36:
            if value[0] == CLASSE3:
                matriz_confusao[CLASSE3][CLASSE3] += 1
            else:
                matriz_confusao[CLASSE3][value[0]] += 1
    return matriz_confusao

def verdadeiro_positivo(matriz_confusao, classe):
    vp = matriz_confusao[classe][classe]
    return vp

def falso_negativo(matriz_confusao, classe):
    fn = 0
    for key in matriz_confusao[classe]:
        if key != classe:
            fn += matriz_confusao[classe][key]
    return fn

def falso_positivo(matriz_confusao, classe):
    fp = 0
    for key1 in matriz_confusao:
        if key1 != classe:
            for key2 in matriz_confusao[key1]:
                if key2 == classe:
                    fp += matriz_confusao[key1][key2]
    return fp

def verdadeiro_negativo(matriz_confusao, classe):
    vn = 0
    for key1 in matriz_confusao:
        if key1 != classe:
            for key2 in matriz_confusao[key1]:
                if key2 != classe:
                    vn += matriz_confusao[key1][key2]
    return vn

def recall(classe):
    vp = verdadeiro_positivo(matriz_confusao, classe)
    fn = falso_negativo(matriz_confusao, classe)
    recall = vp / (vp + fn)
    return recall

def precisao(classe):
    vp = verdadeiro_positivo(matriz_confusao, classe)
    fp = falso_positivo(matriz_confusao, classe)
    precisao = vp / (vp + fp)
    return precisao

def medida_f(classe):
    p = precisao(classe)
    r = recall(classe)
    f = 2 * p * r / (p + r)
    return f

def taxa_fp(classe):
    fp = falso_positivo(matriz_confusao, classe)
    vn = verdadeiro_negativo(matriz_confusao, classe)
    taxa_fp = fp / (fp + vn)
    return taxa_fp

print('1 - Resultados Wine 1NN, usando distância de Euclidiana')

wine = create_list()
treino = wine[18:60] + wine[78:131] + wine[149:178]
teste = wine[0:18] + wine[60:78] + wine[131:149]
distancias = calcular_distancias(treino, teste)
menores = get_1nn(distancias)

print('-------------------------------------------------------')

print('Matriz de confusão: ')
matriz_confusao = matriz_confusao()
print(tuple(matriz_confusao.keys()))
for key in matriz_confusao:
    print(key, tuple(matriz_confusao[key].values()))

print('-------------------------------------------------------')

recall_classe1 = recall(CLASSE1)
print(f'Recall classe 1: {round(recall_classe1 * 100, 2)}%')
recall_classe2 = recall(CLASSE2)
print(f'Recall classe 2: {round(recall_classe2 * 100, 2)}%')
recall_classe3 = recall(CLASSE3)
print(f'Recall classe 3: {round(recall_classe3 * 100, 2)}%')

print('-------------------------------------------------------')

acertos = verdadeiro_positivo(matriz_confusao, CLASSE1) \
    + verdadeiro_positivo(matriz_confusao, CLASSE2) \
    + verdadeiro_positivo(matriz_confusao, CLASSE3)
print(f"Acertos: {round(acertos * 100 / len(menores), 2)}%")

print('-------------------------------------------------------')

precisao_classe1 = precisao(CLASSE1)
print(f'Precisão classe 1: {round(precisao_classe1 * 100, 2)}%')
precisao_classe2 = precisao(CLASSE2)
print(f'Precisão classe 2: {round(precisao_classe2 * 100, 2)}%')
precisao_classe3 = precisao(CLASSE3)
print(f'Precisão classe 3: {round(precisao_classe3 * 100, 2)}%')

print('-------------------------------------------------------')

f_classe1 = medida_f(CLASSE1)
print(f'Medida-F classe 1: {round(f_classe1 * 100, 2)}%')
f_classe2 = medida_f(CLASSE2)
print(f'Medida-F classe 2: {round(f_classe2 * 100, 2)}%')
f_classe3 = medida_f(CLASSE3)
print(f'Medida-F classe 3: {round(f_classe3 * 100, 2)}%')

print('-------------------------------------------------------')

t_vn_classe1 = taxa_fp(CLASSE1)
print(f'Taxa VN classe 1: {round(t_vn_classe1 * 100, 2)}%')
t_vn_classe2 = taxa_fp(CLASSE2)
print(f'Taxa VN classe 2: {round(t_vn_classe2 * 100, 2)}%')
t_vn_classe3 = taxa_fp(CLASSE3)
print(f'Taxa VN classe 3: {round(t_vn_classe3 * 100, 2)}%')



