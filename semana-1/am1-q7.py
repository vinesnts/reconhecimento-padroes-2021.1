CAR_DATA_TREINO = 'semana-1/car1.csv'
CAR_DATA_TESTE = 'semana-1/car2.csv'

def classify(row):
    buying, maint, doors, persons, lug_boot, safety, classe = row.replace('\n', '').split(',')
    if buying in ('low') and maint in ('high') and \
        persons in ('4', 'more') and \
        lug_boot in ('med', 'big') and \
        safety in ('high'):
        return 'vgood' if 'vgood' == classe else None
    if doors == '2' and lug_boot == 'big':
        return 'vgood' if 'vgood' == classe else None
    if buying in ('low', 'med', 'high') and \
        maint in ('vhigh', 'high') and \
        persons in ('4', 'more') and \
        safety in ('high', 'med'):
        return 'acc' if 'acc' == classe else None
    if doors == '5more' and safety in ('med', 'high'):
        return 'acc'
    else:
        return 'unacc' if 'unacc' == classe else None


with open(CAR_DATA_TESTE, 'r') as file:
    rows = file.readlines()
    result = {}
    for row in rows:
        classe = classify(row)
        if classe in result:
            result[classe] += 1
        else:
            result[classe] = 1

    print(result)
    result = [value for key, value in result.items() if key is not None]
    print(sum(result))

