import os, re

def input_contact(): # Функция ввода контакта
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()


    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts(): # Функция Печати контакта
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact(): # Функция поиска контакта
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))

def changeContact():  # Функция изменения информации в контакте
     with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
        numberContact = int(
            input("Input Number of Contact for changing or 0 for return Main Menu: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Input new Lastname: ")
            newName = input("Input new Name: ")
            newPhone = input("Input new Phone: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nContact was successfully changed!")
                input("\n--- press any key ---")
        else:
            return



