import view
import model
import text_fields as txt

def start_pb():
    while True:
        choice = view.main_menu(txt.menu_text, txt.choice_menu, txt.clue_input_menu)
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
                new_contact = view.new_contact(txt.new_name, txt.new_phone, txt.new_comment)
                model.add_contact(new_contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                desired_element = view.desired_contact(txt.find_element)
                founds_contacts = model.find_contact(desired_element)
                view.show_contact(founds_contacts, txt.no_element)
            case 6:
                index_change_contact = view.change_contact_index(txt.change_contact_number, txt.not_number)
                if index_change_contact != None:
                    can_index = model.check_index(index_change_contact)
                    view.check_can_index(can_index, txt.no_index)
                    if can_index:
                        replacing_contact = view.replacing_contact(txt.new_contact_info, txt.new_name, txt.new_phone, txt.new_comment)
                        model.change_contact(replacing_contact, index_change_contact)
                        view.print_info(txt.change_contact_successful)
            case 7:
                index_delete_contact = view.delete_contact_index(txt.delete_contact_number, txt.not_number)
                if index_delete_contact != None:
                    can_index = model.check_index(index_delete_contact)
                    view.check_can_index(can_index, txt.no_index)
                    if can_index:
                        model.delete_contact(index_delete_contact)
                        view.print_info(txt.delete_contact_successful)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        if view.question_save(model.load, txt.need_save):
                            _ = model.save_file(True)
                view.print_info(txt.bye_bye)
                exit()