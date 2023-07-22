# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# spisok = "a a a b c a a d c d d".split()

# slovar ={}
# count = 0                  
# for i in spisok:
#     if i in slovar:
#         slovar [i] += 1 
#         spisok [count] = spisok [count] +'_'+str(slovar [i])
#     else:
#         slovar [i] = 0
#     count +=1

# print (*spisok)

# slovar = {}    

stroka = "a a a b c a a d c d d".split()
result = {}
for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1