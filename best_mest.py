import numpy as np

#  определяем пустые места в зале по рядам и колонкам
def empty_seats(seats):
    x,y = np.where(seats == 0)
    empty_seats = []
    row_1, row_2, row_3, row_4, row_5 = [], [], [], [], []
    rows = [row_1, row_2, row_3, row_4, row_5]
    column_1, column_2, column_3, column_4, column_5 = [], [], [], [], []
    columns = [column_1, column_2, column_3, column_4, column_5]
    for n in range(0, len(x)):
        empty_seats.append([x[n]+1, y[n]+1])
    # print(empty_seats)
    print('Свободные места в зале:')
    for i in empty_seats:
        print(f'ряд {i[0]}, место {i[1]}')
        if i[0] == 1:
            row_1.append(i[1])
        elif i[0] == 2:
            row_2.append(i[1]) 
        elif i[0] == 3:
            row_3.append(i[1])
        elif i[0] == 4:
            row_4.append(i[1]) 
        elif i[0] == 5:
            row_5.append(i[1])

        if i[1] == 1:
            column_1.append(i[0])
        elif i[1] == 2:
            column_2.append(i[0]) 
        elif i[1] == 3:
            column_3.append(i[0])
        elif i[1] == 4:
            column_4.append(i[0]) 
        elif i[1] == 5:
            column_5.append(i[0])
    # print(rows, columns)
    return rows, columns


# вычисляем по каждому месту минимальное расстояние
# до занятого места по полученной оси
def axis_min(axis):
    rigt_q = {}
    left_q = {}
    for q in axis:
        rigt = 0
        if q + 1 == 6:
            rigt = 5  # минимально рабочее решение. требует доработки 
        if q + 1 in axis:
            rigt += 1
            if q + 2 in axis:
                rigt += 1
                if q + 3 in axis:
                    rigt += 1
                    if q + 4 in axis:
                        rigt += 1
        rigt_q[q] = rigt
        left = 0
        a = q - 1
        s = a - 1
        d = s - 1
        if q - 1 == 0:
            left = 5  # минимально рабочее решение. требует доработки 
        if q - 1 in axis:
            left += 1
            if q - 2 in axis:
                left += 1
                if q - 3 in axis:
                    left += 1
                    if q - 4 in axis:
                        left += 1
        left_q[q] = left
    result = comparison(rigt_q,left_q)
    return result
    
def comparison(a,b):    
    result = {}
    for q in a:
        if a[q] <= b[q]:
            result[q] = a[q]
        else:
            result[q] = b[q]
    return result


def main(seats):
    rows_min = []
    columns_min = []
    seats_rows = {}
    seats_columns = {}
    rows, columns = empty_seats(seats)
    for row in rows:
        rows_min.append(axis_min(row)) # передали ось по горизонтали
    for column in columns:
        columns_min.append(axis_min(column)) # передали ось по вертикали
    for q in range(0, 5):
        for w in rows_min[q]:
            seat = f'ряд {q+1} место {w}'
            seats_rows[seat] = rows_min[q][w]

    for q in range(0, 5):
        for w in columns_min[q]:
            seat = f'ряд {w} место {q+1}'
            seats_columns[seat] = columns_min[q][w]        
    result = comparison(seats_rows,seats_columns)
    Keymax = max(result, key=result.get)
    print()
    print(f'лучшее место для Виталия - {Keymax}')

if __name__ == '__main__':

    seats = np.array([[1, 0, 0, 1, 0], 
                    [0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1],
                    [0, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1]])

    main(seats)
