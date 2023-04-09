phone_book = []
start_book = []
PATH = "phone_book.txt"

def get_pb():
    global phone_book
    return phone_book

def load_file():
    global phone_book, start_book
    with open(PATH, "r", encoding= "UTF-8") as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip() .split(" - ")
        phone_book.append({"name" : contact[0],
                            "phone" : contact[1],
                            "comment" : contact[2]})
    start_book = phone_book.copy()