# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for c, v in list_letters.items():
#         if i in v:
#             summ += c
# print(f"Стоимость слова: {summ}")

import re
 
s = input()
d = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3', '[FHVWY]': '4', 'K': '5', '[JX]': '8', '[QZ]': '19'}
for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))