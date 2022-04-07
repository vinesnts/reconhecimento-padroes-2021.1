
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
        try:
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
        except KeyError as e:
            raise KeyError(f'Coluna {str(e)} não existe na base fornecida')