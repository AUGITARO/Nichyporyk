n = int(input("Введите количество оценок: "))
grades = []

for i in range(n):
    grade = float(input(f"Введите оценку {i + 1}: "))
    grades.append(grade)
print("Оценки:", grades)

average_grade = sum(grades) / n
print("Среднее:", average_grade)