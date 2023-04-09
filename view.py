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
        max_len_comment = max([len(contact.get("comment")) for contact in book])
        print(max_len_comment)
        print("\n" + "-" * (47 + max_len_comment))
        for n, contact in enumerate(book, 1):
            print(f"{n:>3}. {contact.get('name'):<25}"
                  f"{contact.get('phone'):<15}"
                  f"{contact.get('comment'):<20}")
        print("-" * (47 + max_len_comment) + "\n")
    else:
        print(message)

def new_contact():
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {"name" : name, "phone" : phone, "comment" : comment}

def confirm(message):
    print()
    answer = input(message + "(y/n) -> ")
    if answer.lower() == "y":
        return True
    else:
        return False

