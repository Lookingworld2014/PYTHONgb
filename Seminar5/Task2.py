# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

from random import randint

num = int(input("Введите количество оценок"))

listOcenok = [randint(1,5) for i in range(num)]

print(*listOcenok)

newspisok = []

for el in listOcenok:
    if el == max(listOcenok):
        newspisok.append(min(listOcenok))
    else:
        newspisok.append(el)    

print(*newspisok)


marks_number = int(input ("Введите количество оценок : "))
marks = [int(input (f'Введите оценку {i} : ')) for i in range(marks_number)]
print(*marks)
max_mark = max(marks)
min_mark = min (marks)
for i in range(marks_number):
    if marks [i] == max_mark : marks [i] =min_mark
#marks = map((lambda x : min_mark if (x==max_mark) else x), marks)
print(*marks)