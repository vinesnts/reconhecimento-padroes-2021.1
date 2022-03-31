import numpy as np
import math

from utils import export_data, load_data

class OrdinalConverter():

    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    def convert_data(self):
        for index, row in enumerate(self.data):
            new_row = {k:v for k,v in row.items()}
            for key, value in row.items():
                if key in self.columns:
                    new_row[key] = self.columns[key][value]
            self.data[index] = new_row
        return self.data

    @staticmethod
    def get_sin_attr(index, length):
        return round(math.sin(2 * math.pi * index / length),2)

    @staticmethod
    def get_cos_attr(index, length):
        return round(math.cos(2 * math.pi * index / length),2)

def main():
    data, columns = load_data('./data/car.csv', sep=',')
    ordinal_converter = OrdinalConverter(data, 
        {
            'buying': {'vhigh': 3, 'high': 2, 'med': 1, 'low': 0},
            'maint': {'vhigh': 3, 'high': 2, 'med': 1, 'low': 0},
            'doors': {'2': 0, '3': 1, '4': 2, '5more': 3},
            'persons': {'2': 0, '4': 1, 'more': 2},
            'lug_boot': {'small': 0, 'med': 1, 'big': 2},
            'safety': {'low': 0, 'med': 1, 'high': 2},
            'class': {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
        })
    data = ordinal_converter.convert_data()

    print(tuple(data[0].keys()))
    [print(tuple(row.values())) for row in data]
    export_data('./data/questao_4_b_export.csv', data, columns)


if __name__ == '__main__':
    main()