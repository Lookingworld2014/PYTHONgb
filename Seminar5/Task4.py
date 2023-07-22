'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5 Output: yes

'''

n = int(input("введите число: "))



# def simpleCheck(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True
i = n-1
def simplerecur(n, i):
    
    if i==1:
        return True
    else:
        if n%i==0:
            return False
        return simplerecur(n, i-1)



print(simplerecur(n, i))





def func(n,count = 2):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif (n % count) == 0:
        return False
    elif count*count > n:
        return True
    else:
        return func(n,count+1)

print(func(n))