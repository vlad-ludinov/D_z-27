import view
import model
import text_fields as txt

def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                new_contact = view.new_contact()
                model.add_contact(new_contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
