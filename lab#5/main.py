# -*- coding: cp1251 -*-
# Определить является ли пятизначное число, введенное с клавиатуры четным. То же самое с четырехзначным.
def is_even_recursive(num):
    if num < 10:
        return num % 2 == 0
    return is_even_recursive(num // 10)

def is_even_loop(num):
    return num % 2 == 0

def check_five_digit():
    num = int(input("Введите пятизначное число: "))
    if 10000 <= num <= 99999:
        if is_even_recursive(num):
            print("Пятизначное число четное (рекурсия).")
        else:
            print("Пятизначное число нечетное (рекурсия).")

        if is_even_loop(num):
            print("Пятизначное число четное (цикл).")
        else:
            print("Пятизначное число нечетное (цикл).")
    else:
        print("Число не является пятизначным.")

def check_four_digit():
    num = int(input("Введите четырехзначное число: "))
    if 1000 <= num <= 9999:
        if is_even_recursive(num):
            print("Четырехзначное число четное (рекурсия).")
        else:
            print("Четырехзначное число нечетное (рекурсия).")

        if is_even_loop(num):
            print("Четырехзначное число четное (цикл).")
        else:
            print("Четырехзначное число нечетное (цикл).")
    else:
        print("Число не является четырехзначным.")

def main():
    check_five_digit()
    check_four_digit()

if __name__ == "__main__":
    main()
