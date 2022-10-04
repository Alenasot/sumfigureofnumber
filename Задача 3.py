# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:20:02 2022

@author: Елена Еремеева
"""
# 3. Найти сумму цифр, входящих в целое натуральное число.
#number = int(input('Введите целое натуральное число: '))
number = 55501

# предпочтительный вариант: пока число не будет равно 0 выполнять действия: прибавлять к сумме остаток от деления на 10, число приравнивать к целому числу от деления на 10

def summa(number):
    summ = 0
    while number != 0:
        summ += number%10
        number = number//10
    return summ

print('Сумма цифр числа:', summa(number))

# Можно создать список из цифр числа и посчитать сумму списка

def summa(number):
    return (sum([int(item) for item in str(number)]))
           
print('Сумма цифр числа:', summa(number))

# Можно пройтись по цифрам числа, переведя его в строку, и прибавлять куждую цифру к сумме

def summa(number):
    summ = 0
    for item in str(number):
        summ += int(item)
    return summ

print('Сумма цифр числа:', summa(number))