import numpy as np
import math

from utils import export_data, load_data

WEEK_DAYS = {
  'sun': 1,
  'mon': 2,
  'tue': 3,
  'wed': 4,
  'thu': 5,
  'fri': 6,
  'sat': 7,
}

MONTHS = {
  'jan': 1,
  'feb': 2,
  'mar': 3,
  'apr': 4,
  'may': 5,
  'jun': 6,
  'jul': 7,
  'aug': 8,
  'sep': 9,
  'oct': 10,
  'nov': 11,
  'dec': 12,
}

class CyclicConverter():

    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    def order_cyclic_table(self):
        for col in self.columns:
            if col == 'month':
                ordered = {}
                for month in self.cyclic_table[col]:
                    ordered[month] = MONTHS[month]
                self.cyclic_table[col] = ordered
            if col == 'day':
                ordered = {}
                for day in self.cyclic_table[col]:
                    ordered[day] = WEEK_DAYS[day]
                self.cyclic_table[col] = ordered

    def create_cyclic_table(self):
        self.cyclic_table = {}
        for col in self.columns:
            possible_values = list(set(row[col] for row in self.data))
            self.cyclic_table[col] = possible_values

        self.order_cyclic_table()
        return self.cyclic_table

    def convert_data(self):
        self.create_cyclic_table()

        for index, row in enumerate(self.data):
            new_row = {k:v for k,v in row.items()}
            for key, value in row.items():
                if key in self.columns:
                    new_row[key] = (
                        CyclicConverter.get_sin_attr(self.cyclic_table[key][value], len(self.cyclic_table[key])),
                        CyclicConverter.get_cos_attr(self.cyclic_table[key][value], len(self.cyclic_table[key])))
            self.data[index] = new_row
        return self.data

    @staticmethod
    def get_sin_attr(index, length):
        return round(math.sin(2 * math.pi * index / length),2)

    @staticmethod
    def get_cos_attr(index, length):
        return round(math.cos(2 * math.pi * index / length),2)

def main():
    data, columns = load_data('./data/forestfires.csv', sep=',')
    cyclic_converter = CyclicConverter(data, ['month', 'day'])
    data = cyclic_converter.convert_data()

    print(tuple(data[0].keys()))
    [print(tuple(row.values())) for row in data]
    export_data('./data/questao_2_b_export.csv', data, columns)


if __name__ == '__main__':
    main()