# list_1 = [1, 2, 3, 4, 7, 8,]
# k = 6
# a = 0
# b = 0
# c = 0

# # Введите ваше решение ниже
# for el in list_1:
#     if el == k:  
#         a = k
#     elif el + 1 == k:
#         b = el
#     elif el - 1 == k:
#         c = el
# if a == k:
#     print(a)
# elif c == 0:
#     print(b)
# elif b == 0:
#     print(c)
# else:
#     print(b,c)
from random import randint
n = 10
list_1 = list(randint(0 , 1) for i in range(n))
print(list_1)