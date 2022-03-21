with open('./wine.csv', 'r') as file:
    rows = file.readlines()
    new_rows = []
    for row in rows:
        new_rows.append(row.split(',')[0:13])

with open('./wine-1.csv', 'w') as file:
    for row in new_rows:
        file.write(f"{','.join(row)}\n")
