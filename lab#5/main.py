# -*- coding: cp1251 -*-
# Определить является ли пятизначное число, введенное с клавиатуры четным. То же самое с четырехзначным.
def is_even(number):
    return number % 2 == 0

number = input("Введите число: ")

if number.isdigit() and (len(number) == 4 or len(number) == 5):
    number = int(number)
    if is_even(number):
        print(f"{number} - четное число.")
    else:
        print(f"{number} - нечетное число.")
else:
    print("Введите корректное четырехзначное или пятизначное число.")
