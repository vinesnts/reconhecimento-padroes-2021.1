from utils import load_data, export_data

class BinaryCategorizer():

    def __init__(self, data: list[dict], columns: list, intervals: tuple[tuple]):
        '''
            - interval: dict = {'value1': 0, 'value2': 0, 'value3': 1, 'value4': 1}
        '''
        self.data = data
        self.columns = columns
        self.intervals = intervals

    def categorize(self, value):
        return self.intervals[value]

    def convert_data(self):
        categorized = []
        for row in self.data:
            new_row = {k:v for k,v in row.items()}
            for col in self.columns:
                new_row[col] = self.categorize(new_row[col])
            categorized.append(new_row)
        self.data = categorized
        return self.data

def main():
    data, columns = load_data('./data/questao_1_b_export.csv')

    intervals = {str(v): (0 if v < 14 else 1) for v in range(0,21)}
    binary_categorizer = BinaryCategorizer(data, ['G3'], intervals)
    data = binary_categorizer.convert_data()
    print(tuple(data[0].keys()))
    [print(tuple(row.values())) for row in data]
    export_data('./data/questao_1_c_export.csv', data, columns)

if __name__ == '__main__':
    main()