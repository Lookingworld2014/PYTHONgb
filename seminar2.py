#Задача No9. Решение в группах
#По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
#Input: 5
#Output: 120

# n=int(input("input n"))
# i=1                 # первое число последовательности
# s=1                 # искомое произведение последовательности чисел
# while n >= i:
#     s=s*i           #вычисляем произведение первого числа на произведение из предыдущего цикла
#     print("Цикл выполнился", i, "раз")
#     print(s)
#     i+=1            #увеличиваем первое число на 1 в цикле
# print (s)    
# print('Цикл окончен')


#Задача No11. Решение в группах
#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#Input: 5 Output: 6


# A=int(input("input A")) # 0 1 1 2 3 5 8 13 21 
# m=0                     #первое число Фибоначчи
# n=1                     #второе число Фибоначчи
# s=0                     #последующее число Фибоначчи
# p=2                     #Определяемый порядковый номер числа Фибоначчи. Присваиваем изначальный счётчик равный 2
               
# while s <= A:
#     if s != A:
#         s=m+n               #вычисление следующего числа Фибоначчи в цикле
#         m=n                 #сдвигаем первое из пары числел Фибоначчи в цикле
#         n=s                 #сдвигаем второе из пары числел Фибоначчи в цикле
#         p=p+1               #считаем порядковый номер числа Фибоначчи в цикле
#     else:
#         print("Порядковый номер введенного числа Фибоначчи:",p)
#         break
# else:
#     print("Ведёное число - не число фибоначчи")

# a = int(input("Введите число - "))
# n = 0
# n1 = 1
# i = 2
# t = 0
# count = 0
# while a > count:
#     count = n + n1
#     t = n1
#     n1 = n1 + n
#     n = t
#     if a == count:
#         break
#     i +=1
# if count != a:
#     print(-1)
# else:
#     print(i+1)

# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81


# from random import randint
# n =  int(input("Ведите число"))
# for i in range(n-1):
#     print(randint(-100, 100), end=', ')
# print(randint(-100,100))
# print("котики")


# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те,
# в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 Output: 2

from random import randint
n =  int(input("Ведите число"))
temp = [randint(-50, 50) for i in range(n)]
print(temp)
count = 0
sklad = 0
for i in range(n-1):
    if temp[i] > 0:
        count += 1
    elif temp[i] <= 0:
        sklad = count
        count = 0
if count > sklad:
    sklad = count
     
print(sklad)

    

# n = int(input("Введите количество дней"))
# count = 0
# max = 0
# for i in range(n):
#     x = int(input())
#     if x>0:
#         count+=1
#     else:
#         if count>max:
#             max = count
#         count = 0
# if count>max:
#     max = count
# print(max)

# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
#Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9



# n = int(input("Введите количество арбузов: "))
# x = int(input())
# minWeigt = x
# maxWeight = x   
# for i in range(n-1):
#     x = int(input())
#     if x<minWeigt:
#         minWeigt = x
#     if x>maxWeight:
#         maxWeight = x    

# print(minWeigt, maxWeight)