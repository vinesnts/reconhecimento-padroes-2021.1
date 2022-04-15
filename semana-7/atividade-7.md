#### Universidade Federal do Agreste de Pernambuco
#### Bacharelado em Ciências da Computação
#### Prof. Tiago Buarque A. de Carvalho
---
## Aprendizagem de Máquina:
### Exercícios sobre Agrupamento
### Aluno: Vinícius Santos de Almeida
---
- 1\. a)
    - Nessa questão, percorri um array que compõe cada valor de K, e em cada iteração fiz o calculo rodei o `KMeans` com 10 iterações, gerando o vetor de y predito, em seguida percorro cada grupo gerado e associo em cada y predito naquele grupo a classe real do índice, ao finalizar para todos os Ks, formato as arrays para criação dos gráficos.
    - A saída foi feita em imagens .png que foram anexas a seguir:
        - ![K=3, grupo=0](saida/questao_1_a_k-3_group-0.png)
        - ![K=3, grupo=1](saida/questao_1_a_k-3_group-1.png)
        - ![K=3, grupo=2](saida/questao_1_a_k-3_group-2.png)
        - ![K=6, grupo=0](saida/questao_1_a_k-6_group-0.png)
        - ![K=6, grupo=1](saida/questao_1_a_k-6_group-1.png)
        - ![K=6, grupo=2](saida/questao_1_a_k-6_group-2.png)
        - ![K=6, grupo=3](saida/questao_1_a_k-6_group-3.png)
        - ![K=6, grupo=4](saida/questao_1_a_k-6_group-4.png)
        - ![K=6, grupo=5](saida/questao_1_a_k-6_group-5.png)
        - ![K=9, grupo=0](saida/questao_1_a_k-9_group-0.png)
        - ![K=9, grupo=1](saida/questao_1_a_k-9_group-1.png)
        - ![K=9, grupo=2](saida/questao_1_a_k-9_group-2.png)
        - ![K=9, grupo=3](saida/questao_1_a_k-9_group-3.png)
        - ![K=9, grupo=4](saida/questao_1_a_k-9_group-4.png)
        - ![K=9, grupo=5](saida/questao_1_a_k-9_group-5.png)
        - ![K=9, grupo=6](saida/questao_1_a_k-9_group-6.png)
        - ![K=9, grupo=7](saida/questao_1_a_k-9_group-7.png)
        - ![K=9, grupo=8](saida/questao_1_a_k-9_group-8.png)
    - Implementação:
        ```python
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

        ```
- 1\. b)
    - Para fazer essa questão foi necessário iterar 10 vezes em cada iteração criando uma nova instância da classe `KMeans` da biblioteca `sklearn`, em cada nova instância o número máximo de iterações é zero e os centróides iniciais são os centróides da iteração anterior, exceto na primeira iteração que são gerados aleatoriamente.
    - Segue as tabelas de média e desvio padrão assim como retornado na saída:
        - Tabela de médias:
        
        |    i    |   3    |   6   |   9   |
        |---|---|---|---|
        | 1 | 2.19 | 2.315 | 2.309 |
        | 2 | 2.199 | 2.292 | 2.3 |
        | 3 | 2.204 | 2.295 | 2.304 |
        | 4 | 2.212 | 2.295 | 2.304 |
        | 5 | 2.225 | 2.295 | 2.304 |
        | 6 | 2.239 | 2.295 | 2.304 |
        | 7 | 2.256 | 2.295 | 2.304 |
        | 8 | 2.27 | 2.295 | 2.304 |
        | 9 | 2.285 | 2.295 | 2.304 |
        | 10 | 2.292 | 2.295 | 2.304 |

        - Tabela de desvios:

        |    i    |   3    |   6   |   9   |
        |---|---|---|---|
        | 1 | 1.48 | 1.584 | 1.54 |
        | 2 | 1.505 | 1.574 | 1.541 |
        | 3 | 1.518 | 1.576 | 1.545 |
        | 4 | 1.53 | 1.576 | 1.545 |
        | 5 | 1.545 | 1.576 | 1.545 |
        | 6 | 1.556 | 1.576 | 1.545 |
        | 7 | 1.567 | 1.576 | 1.545 |
        | 8 | 1.576 | 1.576 | 1.545 |
        | 9 | 1.586 | 1.576 | 1.545 |
        | 10 | 1.589 | 1.576 | 1.545 |

    - Segue a implementação:
        ```python
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

        ```
- 1\. c)
    - A implementação foi feita, porém ao testar a questão 1. b usando a minha implementação, percebe-se que há muitos casos em que o algoritmo agrupa em apenas alguns grupos e não todos, acredito que isso se dá pelo vetor de centróides aleatório com o qual começa a cada tentativa, a biblioteca usada na questão anterior deve oferecer melhores centróides que os meus aleatórios.
    - Segue abaixo a saída de agrupamento para cada k em [3,6,9] na base íris com 10 iterações:
        - `k=3`:
            ```
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1]
            ```
        - `k=6`
            ```
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 4, 4, 0, 3, 0, 3, 0, 0, 4, 0, 0, 0, 3, 3, 0, 3, 3, 3, 3, 0, 0, 3, 0, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 3, 3, 3, 0, 0, 3, 3, 0, 0, 3, 3, 3, 3, 3]
            ```
        - `k=9`
            ```
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 5, 6, 5, 6, 5, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 5, 6, 6, 6, 5, 6, 6, 6, 5, 6, 6, 5]
            ```
    - Segue abaixo a implementação:
        ```python
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

        kmedias = KMedias(X, 3, 10)
        print(kmedias.predict(init=None))
        ```
- 2\. a)
    - Fiz a questão com o auxílio do `StratifiedShuffleSplit` da biblioteca `sklearn` para realizar o split stratificado e o `KMedoids` da biblioteca `sklearn_extra` para executar o k-medoids.
    - A saída dos Y preditos ao executar um Holdout de 50/50 Estratificado foram as seguintes para cada k:
        - 9:
            - `[5 6 5 5 5 5 7 7 7 5 3 7 3 8 5 7 5 4 3 8 5 7 0 5 5 7 8 8 6 7 7 2 5 7 1 6 5
        7 3 6 7 5 5 7 6 6 6 8 5 0 6 7 8 6 6 7 2 6 5 8 4 5 6 1 6 5 5 5 7 5 5 1 5 5
        3]`

        - 18:
            - `[ 4  6  4  4  4  4 15 15 15  4 10 15  0 17  4 15  4 11  0  2  4 15  1  4
        4 15  9 17 14 15 15 13  4  6 16 14  4 15  0 17 15  4  4  6  6 14 14  5
        4  3  6 15  2 14 16 15 11  6  4  8 12  4  9 14 14  4  4  4  6  4  4  7
        4  4  0]`

        - 27:
            - `[ 4 20  4  4  4  4 25  9 25  4 10  9 18 23  4 25  4 17 15  2  4 25 19  4
        4 25  1 14 26 25 25 13  4  9 11 21  4 25 18  6 25  4  4 20 20 24  6  5
        4  3 20 25  2  6 11 25 17 20  4  8 12  4 16  0 22  4  4  4 20  4  4  7
        4  4 15]`

        - 45:
            - `[41 33 44 41 41 44 36 39 40 41 10 39 32 31 41 43 41 17 18 30 41 43 19 44
        44 37  1 14 28 40 43 13 41 38 11 21 41 43 29  9 34 41 44 35 25 24  6  5
        41  3 23 43  2 20 22 37  4 27 44  8 12 41 16  0 26 44 44 41 42 44 41  7
        44 44 15]`

        - 72:
            - `[54 37 70  3  4  5  6 61  8  9 10 11 12 13 55 63 16 17 18 19 20 68 22 23
        62 25 26 27 28 29 30 31 60 33 34 35 36 68 38 39 40 59 57 43 44 45 46 47
        64 49 50 63 52 53  0 51 48 42 58 41 32 69 24 21 15 65 70 67 14 66 71  7
        2 56  1]`
    - A implementação ficou como a seguir:
        ```python
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
        ```
- 2\. b)
    - Fazendo o procedimento solicitado, segue a saída obtida com a taxa de acerto para cada classe em cada k:
        - K = 9:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 85.714
            - Taxa de acerto versicolor: 95.455
        - K = 18:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 85.185
            - Taxa de acerto versicolor: 91.304
        - K = 27:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 92.308
            - Taxa de acerto versicolor: 95.833
        - K = 45:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 88.889
            - Taxa de acerto versicolor: 95.652
        - K = 72:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 88.889
            - Taxa de acerto versicolor: 95.652
    - Implementação:
        ```python
        import numpy as np

        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.model_selection import StratifiedShuffleSplit
        from sklearn_extra.cluster import KMedoids

        from utils import load_data

        def calc_taxa_acerto(acertos, erros, classe):
            return round((acertos[classe] / (acertos[classe] + erros[classe])) * 100, 3)

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
                kmedoids.fit(X_train)
                centroids = kmedoids.cluster_centers_
                X_train_reduced = []
                y_train_reduced = []
                for i, row in enumerate(X_train):
                    for centroid in centroids:
                        equal = True
                        for x_value, centroid_value in zip(row, centroid):
                            if x_value != centroid_value:
                                equal = False
                                break
                        if equal:
                            X_train_reduced.append(row)
                            y_train_reduced.append(y_train[i])

                knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")
                knn.fit(X_train_reduced, y_train_reduced)

                predicts = knn.predict(X_test)
                acertos = {
                    'setosa': 0,
                    'virginica': 0,
                    'versicolor': 0
                }
                erros = {
                    'setosa': 0,
                    'virginica': 0,
                    'versicolor': 0
                }
                for i, predict in enumerate(predicts):
                    if y_test[i] == predict:
                        acertos[predict] += 1
                    else:
                        erros[predict] += 1
                print(f'- K = {k}:')
                for classe in acertos:
                    print(f' - Taxa de acerto {classe}: {calc_taxa_acerto(acertos,erros,classe)}')
        ```
- 2\. c) Para essa questão foi necessário apenas usar o `timeit` do python. Ao analisar o resultado, é interessante notar que o tempo de classificação é menor quanto maior o K.
    - Saída:
        - K = 9:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 92.593
            - Taxa de acerto versicolor: 100.0
            - Tempo em 9: 0.002654112999152858
        - K = 18:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 95.833
            - Taxa de acerto versicolor: 92.308
            - Tempo em 18: 0.0019247919990448281
        - K = 27:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 92.593
            - Taxa de acerto versicolor: 100.0
            - Tempo em 27: 0.0024530160007998347
        - K = 45:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 92.0
            - Taxa de acerto versicolor: 92.0
            - Tempo em 45: 0.0024530679947929457
        - K = 72:
            - Taxa de acerto setosa: 100.0
            - Taxa de acerto virginica: 92.308
            - Taxa de acerto versicolor: 95.833
            - Tempo em 72: 0.001998302999709267
    - Implementação (apenas o que muda da questão anterior):
        ```python
        ...
        start = timeit.default_timer()
        knn.fit(X_train_reduced, y_train_reduced)

        predicts = knn.predict(X_test)
        stop = timeit.default_timer()
        ...
        print(f'- Tempo em {k}: {stop - start}')
        ```
- 3\. a)