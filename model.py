phone_book = []
start_book = []
load = False
PATH = "phone_book.txt"

def get_pb():
    global phone_book
    return phone_book

def load_file():
    global phone_book, start_book, load
    load = True
    with open(PATH, "r", encoding= "UTF-8") as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip() .split(" - ")
        phone_book.append({"name" : contact[0],
                            "phone" : contact[1],
                            "comment" : contact[2]})
    start_book = phone_book.copy()

def add_contact(contact):
    global phone_book
    phone_book.append(contact)

def save_file(was_load):
    global phone_book
    if was_load:
        data = []
        for contact in phone_book:
            data.append(" - ".join([value for value in contact.values()]))
        data = "\n".join(data)
        with open(PATH, "w", encoding="UTF-8") as file:
            file.write(data)
        return True
    return False

def find_contact(desired_element):
    global phone_book
    found_contacts = []
    for n, contact in enumerate(phone_book, 1):
        for element in contact.values():
            if element == desired_element:
                found_contacts.append((n, contact))
    return found_contacts

def exit_pb():
    global phone_book, start_book
    if phone_book == start_book:
        return False
    else:
        return True
    
def change_contact(contact, index):
    global phone_book
    pb = ["name", "phone", "comment"]
    for i in range(len(contact)):
        if contact[i] != "":
            phone_book[index][pb[i]] = contact[i]

def check_index(index):
    global phone_book
    if -1 < index < len(phone_book):
        return True
    return False

def delete_contact(index):
    global phone_book
    phone_book.pop(index)