import random

Y = [random.randint(1, 100) for _ in range(15)]
print("Список Y:", Y)

min_element = min(Y)
min_index = Y.index(min_element)

print("Наименьший элемент:", min_element)
print("Порядковый номер наименьшего элемента:", min_index + 1)