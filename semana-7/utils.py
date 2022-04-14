import random

def load_data(filename, sep=';'):
    columns = None
    data = []
    with open(filename, 'r') as file:
        for index, row in enumerate(file.readlines()):
            row_list = row.strip().replace("\"", "").split(sep)
            if index == 0:
                columns = [col for col in row_list]
            if index > 0:
                data.append(
                    {columns[index]: value for index, value in enumerate(row_list)})
    return data, columns

def export_data(filename, data, columns):
    with open(filename, 'w') as file:
        file.write(';'.join(columns))
        file.write('\n')
        for row in data:
            file.write(';'.join([str(value) for value in row.values()]))
            file.write('\n')

def split_train_test(data: list, train_size: int, by_columns: list):
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    count_columns = {col: 0 for col in by_columns}
    for row in data:
        for k, v in row.items():
            for col in by_columns:
                if count_columns[col] < train_size \
                        and k == col and v:
                    X_train.append([float(v) for k, v in row.items() if k not in by_columns])
                    y_train.append({k:int(v) for k, v in row.items() if k in by_columns})
                    count_columns[col] += 1
                elif count_columns[col] >= train_size \
                    and k == col and v:
                    X_test.append([float(v) for k, v in row.items() if k not in by_columns])
                    y_test.append({k: int(v) for k, v in row.items() if k in by_columns})
    y_train = {col: [v[col] for v in y_train] for col in by_columns}
    y_test= {col: [v[col] for v in y_test] for col in by_columns}
    return X_train, y_train, X_test, y_test

def random_zero_one():
    return round(random.uniform(0, 1), 1)

    
