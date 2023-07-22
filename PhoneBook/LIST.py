# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .csv. Фамилия, имя, комментарий, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


filename = 'phonebook.csv'

# def read_csv(filename: str) -> list: #функция читает файл phonebook.csv
#     data = []
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     with open(filename, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)
#         #fin.close()
#     return data
    
# data = read_csv(filename)
# for i in data:
#     print(i)

#from pprint import pprint
#pprint(read_csv(filename))


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        fields = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(fout, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Такой абонент отсутвует"


def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой абонент отсутвует"


def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)


def get_new_user() -> str:
    print("Введите данные нового абонента в формате 'Фамилия, Имя, Телефон, Описание': ")
    user_data = input()
    return user_data


def get_search_name() -> str:
    print("Введите фамилию для поиска: ")
    last_name = input()
    return last_name


def get_search_number() -> str:
    print("Введите номер телефона для поиска: ")
    phone_number = input()
    return phone_number


def get_file_name() -> str:
    print("Введите название файла: ")
    file_name = input()
    return file_name


def print_result(data: list):
    for el in data:
        print(f"{el.get('Фамилия')}, {el.get('Имя')}, {el.get('Телефон')}, {el.get('Описание')}")

        
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

work_with_phonebook() 