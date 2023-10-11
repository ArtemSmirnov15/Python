"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной """
from logger import choose_action, import_data, read_file_to_dict, read_file_to_list, search_parameters, find_number, get_new_number,add_phone_number,\
      show_phonebook, search_to_modify, change_phone_number, delete_contact, print_contacts



if __name__ == '__main__':
    choose_action
    file = 'Phonebook.txt'
    choose_action(file)