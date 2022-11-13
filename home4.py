# 1. Вычислить число c заданной точностью d

#Пример:

#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

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

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
from sympy import symbols
from math import prod
 
max_val=100
k = int(input())
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(-max_val ,max_val) for i in range(k)]+[randint(1,max_val)]
x = symbols('x')
print (sum(map(prod,zip(koeff,[x**i for i in range(k+1)]))))

# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from itertools import *
from Task033 import get_polynomial
import os
os.system("cls")


file1 = 'task004_1.txt'
file2 = 'task004_2.txt'


def read_pol(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):  # удалили "хвостик" и порезали" строку на массив , разделитель знак " + "
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol


pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)
print('_'*30)
print(convert_pol(pol1))
print(convert_pol(pol2))
pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))
print(pol1_coef)
print(pol2_coef)
print('_'*30)

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
print(sum_coef)
sum_coef = sum_coef[::-1]
print(sum_coef)
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print(sum_pol)
with open('task004.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)