from csv import DictWriter, DictReader
from os.path import exists

file_name = 'phone.csv'
file_name_to_copy = 'copied_phone.csv'


def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера телефона')
            else:
                flag = True
        except ValueError:
            print('Не валидный номер телефона. Попробуйте снова.')

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def find_and_copy_row(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        flag = False
        while not flag:
            try:
                row = int(input('Введите номер строки для копирования: '))
                checking_row = list(f_r)[row - 1]
                flag = True
            except ValueError:
                print('Введена не цифра, попробуйте снова.')

            except IndexError:
                print('Такого номера строки не существует, попробуйте снова.')

        return checking_row
    #НЕ МОГУ ПОНЯТЬ КАК ЗАНОВО СДЕЛАТЬ ПРОВЕРКУ ЗНАЧЕНИЯ row.
    #ЕСЛИ ОДИН РАЗ ВВЕЛ НЕПРАВИЛЬНОЕ ЗНАЧЕНИЕ, ТО ЗНАЧЕНИЯ КОТОРЫЕ БЫЛИ ВВЕДЕНЫ РАНЬШЕ НЕ РАБОТАЮТ!!!! ПОМОГИТЕ
    #ТАКЖЕ НЕ РАБОТАЕТ q


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            res = find_and_copy_row(file_name)
            print(f'Скопирована строка: {res}')
            print(res['Имя'])
            if not exists(file_name_to_copy):
                create_file(file_name_to_copy)
            write_file(file_name_to_copy,[res['Имя'], res['Фамилия'], res['Телефон']])
            print(f'{res} успешно скопирован в файл {file_name_to_copy}!')



if __name__ == '__main__':
    main()
