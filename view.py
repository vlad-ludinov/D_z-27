

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

def print_info(message):
    print("\n" + "-" * len(message))
    print(message)
    print("-" * len(message) + "\n")

def show_contact(book: list[dict], message: str):
    if book:
        print("\n" + "-" * 63)
        for n, contact in enumerate(book, 1):
            print(f"{n:>3}. {contact.get('name'):<20}"
                  f"{contact.get('phone'):<20}"
                  f"{contact.get('comment'):<20}")
        print("-" * 63 + "\n")
    else:
        print(message)