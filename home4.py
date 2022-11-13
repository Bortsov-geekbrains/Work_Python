# 1. Вычислить число c заданной точностью d

#Пример:

#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#from math import pi

d =  int(input())
print(round(pi, d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

num = int(input())
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(lst)