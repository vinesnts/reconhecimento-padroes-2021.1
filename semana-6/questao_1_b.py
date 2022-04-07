from utils import load_data, random_zero_one, split_train_test

from non_binary_categorizer import NonBinaryConverter


class IrisNeuron():

    def __init__(self, N: float = 0.5, max_error: int = 0, limit_epoch: int = None):
        self.weights, self.weights_hist, self.X, self.Y, self.train_class = [], [], None, None, None
        self.N = N
        self.max_error = max_error
        self.limit_epoch = limit_epoch
        print()

    def fit(self, X: list[list], y: list) -> None:
        self.X = X
        self.y = y

    def train(self, train_class: str) -> list:
        self.train_class = train_class
        total_errors = 1
        epoch = 0
        while total_errors > self.max_error \
            or epoch < self.limit_epoch:
            epoch += 1
            print(f'Epoca #{epoch}')
            total_errors = 0
            for i, (x, y) in enumerate(zip(self.X, self.y[train_class])):
                delta = y - IrisNeuron.f(x, self.weights)
                error = delta * delta
                total_errors += error
                if error > 0:
                    self.weights_hist.append([w for w in self.weights])
                    for j, (w_j, x_j) in enumerate(zip(self.weights, x)):
                        self.weights[j] = w_j + self.N * x_j * delta
            print(f'Total de erros: {total_errors}')
        return self.weights

    def test(self, X: list[list], y: list) -> int:
        total_errors = 0
        for x, y in zip(X, y[self.train_class]):
            delta = y - IrisNeuron.f(x, self.weights)
            error = delta * delta
            total_errors += error
        return total_errors

    def set_weights(self, w: list) -> None:
        self.weights = w

    def generate_weights(self, n_columns: int, random: bool = False) -> list:
        weights = [random_zero_one() if random else 0 for i in range(0, n_columns)]
        self.weights = weights
        return self.weights

    @staticmethod
    def f(x: list, w: list) -> int:
        v = 0
        for x_i, w_i in zip(x, w):
            v += x_i * w_i
        return 1 if v > 0 else 0


def main():
    # Load data from file
    data, _ = load_data('./data/iris.csv', ',')

    # Convert categoric attributes to numeric
    nb_converter = NonBinaryConverter(data, ['iris'])
    data, columns = nb_converter.convert_data(), nb_converter.generate_columns()

    # Select sample from data
    classes = ['iris_setosa', 'iris_versicolor', 'iris_virginica']
    X_train, y_train, X_test, y_test = split_train_test(data, train_size=25, by_columns=classes)

    # Init iris train neuron
    neuron = IrisNeuron(limit_epoch=100)
    
    # Add train X and y to neuron
    neuron.fit(X_train, y_train)

    # Generate weights list with n_columns, all values will be 0
    neuron.generate_weights(n_columns=len(X_train[0]), random=False)

    # Train iris_virginica
    neuron.train(train_class='iris_virginica')

    # Show training iris_virginica
    print(f'Histórico de pesos: ')
    [print(w) for w in neuron.weights_hist]
    print(f'Peso definido: ')
    print(neuron.weights)

    # Test iris_virginica
    errors = neuron.test(X_test, y_test)
    print(f'Número de erros no teste: {errors}')

if __name__ == "__main__":
    main()