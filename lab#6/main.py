# -*- coding: cp1251 -*-
def replace_long_lines(input_file, output_file, max_length):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if len(line.strip()) > max_length:
                file.write("!!!\n")
            else:
                file.write(line)


# Пример использования
input_filename = 'input.txt'  # Имя входного файла
output_filename = 'output.txt'  # Имя выходного файла
max_length = 50  # Максимальная длина строки

replace_long_lines(input_filename, output_filename, max_length)