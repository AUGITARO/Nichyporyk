# -*- coding: cp1251 -*-
# Составить программу, которая формирует массив случайных двухзначных чисел из 150 элементов,
# выводит индексы и значения максимального и минимального элемента, а также выводит индексы тех элементов,
# которые находятся между минимальным и максимальным элементом и являются четными

# Программа должна считать количество шагов выполненных при работе с массивом и время затраченное на поиск.
# Для каждого алгоритма провести не менее 15 опытов, результаты опытов (время и количество шагов)
# записать в файл ( файл с возможностью до записи данных),
# рассчитать среднее время работы программы.


import random
import time


def generate_array(size):
    return [random.randint(10, 99) for _ in range(size)]


def find_min_max(arr):
    min_index = max_index = 0
    min_value = max_value = arr[0]
    steps = 0
    for i, num in enumerate(arr):
        steps += 1
        if num < min_value:
            min_value, min_index = num, i
        elif num > max_value:
            max_value, max_index = num, i
    return min_index, min_value, max_index, max_value, steps


def find_even_between(arr, min_index, max_index):
    evens = []
    for i in range(min_index + 1, max_index):
        if arr[i] % 2 == 0:
            evens.append(i)
    return evens


def main():
    size = 150
    experiments = 15
    results = []

    for _ in range(experiments):
        arr = generate_array(size)
        start_time = time.time()

        min_index, min_value, max_index, max_value, steps = find_min_max(arr)
        evens = find_even_between(arr, min_index, max_index)

        elapsed_time = time.time() - start_time
        results.append((elapsed_time, steps))

        with open("results2.txt", "a") as file:
            file.write(
                f"Мин: {min_value} на {min_index}, Макс: {max_value} на {max_index}, Четные: {evens}, Время: {elapsed_time:.6f}, Шаги: {steps}\n")

    avg_time = sum(result[0] for result in results) / experiments
    print(f"Время: {avg_time:.6f} секунд")


if __name__ == "__main__":
    main()
