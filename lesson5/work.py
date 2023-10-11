# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
for i in range(list_1):
    if min_number <= list_1[i] <= max_number:
        print(list_1.index(i)) 
