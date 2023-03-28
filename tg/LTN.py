def ltn(number):
#number = input('Задайте интересующий номер сети ')
    number = int(number)
    bin_number = bin(number)[2:]
    diapazon = range(32)
    last_num = []
    for i in diapazon:
        if 2**i == number:
            last_num.clear()
            last_num = 2**i
            result = ['Заданый номер сети ' + str(number),
                      'Отсутствуют входящие сети',
                      'Представление в двоичном коде:',
                      str(bin(last_num)[2:])]
            return '\n'.join(result)
        if 2**i < number:
            last_num.append(2**i)
        else:
            last_num.reverse()
            break



    sum = 0
    itog = []

    for i in range(len(last_num)):
        sum += last_num[i]

        if sum == number:
            itog.append(int(last_num[i]))
            break

        if sum > number:
            sum -= last_num[i]
            continue

        if sum < number:
            itog.append(int(last_num[i]))
            continue

    itog.insert(0, number)

    # Определение диапазонов матрицы
    w = len(bin_number) # Количество столбцов
    h = len(itog) # Количество строк
    # Создание матрицы
    Matrix = [[0 for y in range(w)] for x in range(h)]

    for i in range(h):
        bin_num = bin(itog[i])[2:]

        if len(bin_num) < w:
            bin_num = '0' * (w - len(bin_num)) + bin_num

        for j in range(w):
            Matrix[i][j] = int(bin_num[j])

    result = ['Заданый номер сети ' + str(number),
              'Список входящих сетей ' + str(itog[1:]),
              'Представление в двоичном коде:']

    for row in Matrix:
        result.append(str(row))

    return '\n'.join(result)