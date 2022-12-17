from import_export import write_data
from import_export import read_data
from controller import*
from function import print_data


def select_operation():
    
    while True:

        print('''\nКоманды выбора меню:
        Добавить контакт : - 1
        Удалить контакт - 2
        Просмотр всех записей - 3
        Поиск контакта - 4
        Выход - 0 \n''')

        menu_selection = input('Введите номер меню: > ')

        if menu_selection == '1':
            list_add=input_data()
            write_data(list_add,sep=", ")
        elif menu_selection == '2':
            a=1
        elif menu_selection == '3':
            data = read_data()
            print_data(data)
        elif menu_selection == '4':
            # del_memb(data)
            a=1
        elif menu_selection == '0':
            print("Работа завершена")
            raise SystemExit
