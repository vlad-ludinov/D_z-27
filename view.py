import text_fields as txt

def main_menu():
    print(txt.menu_text)
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print(txt.clue_input_menu)

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

def new_contact():
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {"name" : name, "phone" : phone, "comment" : comment}
