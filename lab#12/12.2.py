commentators = set()
while True:
    user_input = input("Введите комментарий (имя: комментарий) или нажмите Enter для завершения: ")

    if user_input == "":
        break
    try:
        name, comment = user_input.split(':', 1)  # Разделяем только на первое вхождение ':'
        name = name.strip()  # Убираем лишние пробелы
        commentators.add(name)  # Добавляем имя в множество
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите данные в формате 'имя: комментарий'.")

# Выводим общее число уникальных комментаторов
print(f"Общее число уникальных комментаторов: {len(commentators)}")
