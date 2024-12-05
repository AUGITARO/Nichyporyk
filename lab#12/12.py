things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубкашка': 300}

d = {}
while True:
    user_input = input("Введите предмет и вес (предмет=вес) или нажмите Enter для завершения: ")

    if user_input == "":
        break

    try:
        item, weight = user_input.split('=')
        item = item.strip()  # Убираем лишние пробелы
        weight = int(weight.strip())  # Преобразуем вес в целое число
        d[item] = weight  # Добавляем в словарь d
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите данные в формате предмет=вес.")

things.update(d)


print("Обновленный словарь предметов:")
for item, weight in things.items():
    print(f"{item}: {weight}")
