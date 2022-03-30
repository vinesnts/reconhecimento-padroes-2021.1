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