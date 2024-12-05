import random
numbers = [random.uniform(0, 10) for _ in range(10)]
numbers.sort(reverse=True)
print("Список до сортировки:", numbers)
print("Список после сортировки по убыванию:", numbers)