

def main_menu():
    print("""Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    7. Удалить контакт
    8. Выход""")
    while True:
        choice = input("Выберите пункт меню: ")
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print("Введите ЧИСЛО от 1 до 8")
