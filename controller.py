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
                need_save = view.question_save(model.load, txt.need_save)
                save = model.save_file(need_save)
                view.print_info_save(save, txt.save_successful)
            case 3:
                pb = list(enumerate(model.get_pb(), 1))
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                new_contact = view.new_contact()
                model.add_contact(new_contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                desired_element = view.desired_contact(txt.find_element)
                founds_contacts = model.find_contact(desired_element)
                view.show_contact(founds_contacts, txt.no_element)
            case 6:
                pass
            case 7:
                pass
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()