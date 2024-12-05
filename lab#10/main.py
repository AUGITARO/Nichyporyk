# -*- coding: cp1251 -*-
import queue

def process_numbers(file_path):
    positive_queue = queue.Queue()
    negative_queue = queue.Queue()

    # Чтение файла и распределение чисел
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            if number >= 0:
                positive_queue.put(number)
            else:
                negative_queue.put(number)

    # Печать положительных чисел
    while not positive_queue.empty():
        print(positive_queue.get())

    # Печать отрицательных чисел
    while not negative_queue.empty():
        print(negative_queue.get())

# Использование функции
process_numbers('numbers.txt')
