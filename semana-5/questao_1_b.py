from utils import load_data, export_data

class BinaryConverter():

    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    def values_to_binary(self):
        possible_values = {}
        for key in self.columns:
            values = set()
            for r in self.data:
                values.add(r[key])

            possible_values[key] = values

        new_values = {}
        for key, value in possible_values.items():
            new_values[key] = dict(zip(value, (0,1)))

        return new_values

    def convert_data(self):
        b_values = self.values_to_binary()

        for index, row in enumerate(self.data):
            row_converted = row
            for key, value in row.items():
                if key in self.columns:
                    row_converted[key] = b_values[key][value]
                else:
                    row_converted[key] = value
            self.data[index] = row_converted

        return self.data

class NonBinaryConverter():

    def __init__(self, data, columns):
        self.data = data
        self.columns = columns
        print()

    def generate_columns(self):
        columns = []
        for column in self.data[0]:
            columns.append(column)
        return columns

    def new_columns(self):
        new_columns = {}
        for key in self.columns:
            values = set()
            for r in self.data:
                values.add(r[key])

            new_columns[key] = values

        return new_columns

    def convert_data(self):
        new_columns = self.new_columns()

        new_data = []
        for index, row in enumerate(self.data):
            row_converted = {i: v for i, v in row.items()}
            for key, value in row.items():
                if key in self.columns:
                    for column in new_columns[key]:
                        new_col_name = f'{key}_{column}'
                        if value == column:
                            row_converted[new_col_name] = 1
                        else:
                            row_converted[new_col_name] = 0
            for column in self.columns:
                del row_converted[column]
            new_data.append(row_converted)

        self.data = new_data
        return self.data

def main():
    data, _ = load_data('./data/student-mat.csv')

    binary_converter = BinaryConverter(data, ['sex','school','address','famsize','Pstatus','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic'])
    data = binary_converter.convert_data()
    
    nonbinary_converter = NonBinaryConverter(data, ['Mjob','Fjob','reason','guardian'])
    data = nonbinary_converter.convert_data()

    print(tuple(data[0].keys()))
    [print(tuple(row.values())) for row in data]
    export_data('./data/questao_1_b_export.csv', data, nonbinary_converter.generate_columns())

if __name__ == '__main__':
    main()