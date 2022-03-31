import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit, train_test_split
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score

from my_kneighbors_kfold_classifier import KNeighborsKFoldClassifier

from utils import load_data, export_data

class RescaleStdConverter():

    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    def map_columns_values(self):
        mapped_values = {}
        for col in self.columns:
            mapped_values[col] = np.array([])
            for row in self.data:
                for k,v in row.items():
                    if k not in mapped_values:
                        mapped_values[k] = np.array([float(v)])
                    else:
                        mapped_values[k] = np.append(mapped_values[k], float(v))
        return mapped_values

    @staticmethod
    def calc_rescale(v, min, max):
        return round((v - min) / (max - min),2)

    def rescale_data(self):
        mapped_values = self.map_columns_values()
        self.rescaled_data = []
        for i, row in enumerate(self.data):
            new_row = {k:v for k,v in row.items()}
            for k, v in row.items():
                if k in self.columns:
                    max = mapped_values[k].max()
                    min = mapped_values[k].min()
                    new_row[k] = RescaleStdConverter.calc_rescale(float(v), min, max)
                else:
                    new_row[k] = v
            self.rescaled_data.append(new_row)
        return self.rescaled_data

    @staticmethod
    def calc_std(v, avg, std):
        return round((v - avg) / std, 2)

    def standardize_data(self):
        mapped_values = self.map_columns_values()
        self.standardized_data = []
        for i, row in enumerate(self.data):
            new_row = {k:v for k,v in row.items()}
            for k, v in row.items():
                if k in self.columns:
                    avg = np.average(mapped_values[k])
                    std = mapped_values[k].std()
                    new_row[k] = RescaleStdConverter.calc_std(float(v), avg, std)
                else:
                    new_row[k] = v
            self.standardized_data.append(new_row)
        return self.standardized_data

def main():
    data, columns = load_data('./data/wine.csv', sep=',')
    rescaler_sdt = RescaleStdConverter(data, columns[1:])
    
    rescaled = rescaler_sdt.rescale_data()
    export_data('./data/questao_5_scaled.csv', rescaled, columns)
    standardized = rescaler_sdt.rescale_data()
    export_data('./data/questao_5_std.csv', standardized, columns)

    X = np.array([tuple([float(x) for x in list(row.values())[1:]]) for row in data])
    y = np.ravel([float(row['class']) for row in data])
    knn_kfold = KNeighborsKFoldClassifier(X, y)
    knn_kfold.classify()
    print(f'Intervalo confiança original: {knn_kfold.intervalo_confianca()}')

    data_scaled, _ = load_data('./data/questao_5_scaled.csv')
    X = np.array([tuple([float(x) for x in list(row.values())[1:]]) for row in data_scaled])
    y = np.ravel([float(row['class']) for row in data_scaled])
    knn_kfold = KNeighborsKFoldClassifier(X, y)
    knn_kfold.classify()
    print(f'Intervalo confiança intervalo [0,1]: {knn_kfold.intervalo_confianca()}')

    data_std, _ = load_data('./data/questao_5_std.csv')
    X = np.array([tuple([float(x) for x in list(row.values())[1:]]) for row in data_std])
    y = np.ravel([float(row['class']) for row in data_std])
    knn_kfold = KNeighborsKFoldClassifier(X, y)
    knn_kfold.classify()
    print(f'Intervalo confiança padronização: {knn_kfold.intervalo_confianca()}')


if __name__ == '__main__':
    main()