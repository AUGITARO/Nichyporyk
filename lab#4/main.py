# -*- coding: cp1251 -*-
# Составь программу на python, которая формирует массив двухзначных чисел из 100 элементов,
#   выводит индексы элементов, которые имеют одинаковые значения.
# Программа должна считать количество шагов выполненных при работе с массивом и время затраченное на поиск.
# Для каждого алгоритма провести не менее 15 опытов, результаты опытов (время и количество шагов)
# записать в файл ( файл с возможностью до записи данных),
# рассчитать среднее время работы программы.


import random
import time
import numpy as np

def generate_array(size):
    return [random.randint(10, 99) for _ in range(size)]

def find_duplicates(arr):
    indices = {}
    steps = 0
    for index, value in enumerate(arr):
        steps += 1
        if value in indices:
            indices[value].append(index)
        else:
            indices[value] = [index]
    return {key: val for key, val in indices.items() if len(val) > 1}, steps

def main():
    size = 100
    num_trials = 15
    results = []

    for _ in range(num_trials):
        arr = generate_array(size)
        start_time = time.time()
        duplicates, steps = find_duplicates(arr)
        elapsed_time = time.time() - start_time

        results.append((elapsed_time, steps))

        with open('results.txt', 'a') as f:
            f.write(f"Итерация номер: {_}")
            f.write(f"Затраченное время: {elapsed_time:.5f}s, Шаги: {steps},\n Дубликаты: {duplicates}\n")

    avg_time = np.mean([result[0] for result in results])
    print(f"Average Time over {num_trials} trials: {avg_time:.5f}s")

if __name__ == "__main__":
    main()
