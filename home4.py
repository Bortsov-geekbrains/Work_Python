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

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input().split()))
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(new_lst)

