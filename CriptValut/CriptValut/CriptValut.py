import csv

name = []
market_cap = []
price = []

with open('currencies22.csv', 'r') as File:
    F_reader = csv.reader(File, delimiter=";")
    for row in F_reader:
        name.append(row[0])
        market_cap.append(row[1])
        price.append(row[2])

def poisk():
    i = 0
    count = 0
    while 1:
        cript = input('Введите название криптовалюты: ')
        for i in range(25):
            if cript == name[i]:
                print('Наименование: ', name[i], '\nРыночная капитализация: ', market_cap[i],
                    '\nСтоимость 1 ед. в долларах США: ', price[i])
                break
            else:
                count += 1

        if count >= 25 and cript != name[i]:
            print('О такой криптовалюте нет информации')
            count = 0
poisk()
