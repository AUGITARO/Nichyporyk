# -*- coding: cp1251 -*-
import csv

def filter_employees(input_file, output_file, salary_threshold):
    employees = []

    # Чтение данных из входного файла
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Пропускаем заголовок

        for row in reader:
            # Считываем данные о сотруднике
            fio = row[0]
            year_of_hire = int(row[1])
            position = row[2]
            salary = float(row[3])
            experience = int(row[4])

            # Проверяем, если зарплата ниже заданного уровня
            if salary < salary_threshold:
                employees.append((fio, year_of_hire, position, salary, experience))

    # Сортировка сотрудников по рабочему стажу
    employees.sort(key=lambda x: x[4])  # Сортируем по стажу

    # Запись отфильтрованных данных в выходной файл
    with open(output_file, mode='w', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['ФИО', 'Год принятия', 'Должность', 'Зарплата', 'Стаж'])  # Заголовок
        for employee in employees:
            writer.writerow(employee)

# Параметры
input_file = 'employees.csv'  # Входной файл
output_file = 'filtered_employees.csv'  # Выходной файл
salary_threshold = 50000  # Порог зарплаты

# Вызов функции
filter_employees(input_file, output_file, salary_threshold)

print(f"Данные о сотрудниках с зарплатой ниже {salary_threshold} записаны в файл '{output_file}'.")