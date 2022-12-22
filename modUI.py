from modDB import write_contact as wc


def get_main_menu():
    while True:
        str_message ='Для взаимодействия с телефонным справочником введите:\n\
            1 - для получения данных контакта\n\
            2 - для добавления контакта\n\
            3 - для импорта в телефонный справочник\n\
            4 - для экспорта из телефонного справочника\n\
            5 - для сброса данных в телефонном справочнике\n\
            6 - для выхода из телефонного справочника\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 6, 1)
        if int_answer is None: print('Невернный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            return menu_get_contact()
        case 2:
            return menu_add_contact()
        case 3:
            return import_menu()
        case 4:
            return export_menu()
        case 5:
            return drop_menu()
        case 6:
            return exit_menu()


def menu_get_contact():
    while True:
        str_message ='Введите:\n\
            1 - для получения данных по фамилии контакта\n\
            2 - для получения данных по фамилии и имени контакта\n\
            3 - для возврата в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 3, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    str_message = 'Введите фамилию контакта: '
    match int_answer:
        case 1:
            return [1, get_string(str_message), '']
        case 2:
            str_family = get_string(str_message)
            str_message = 'Введите имя контакта: '
            str_name = get_string(str_message)
            return [1, str_family, str_name]
        case 3:
            return get_main_menu()


def menu_add_contact():
    while True:
        str_message ='Введите:\n\
            1 - для добавления контакта\n\
            2 - для возврата в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 2, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            str_message = 'Введите номер телефона в формате 8**********: '
            int_phone = get_phone_number(str_message)
            str_message = 'Введите имя контакта: '
            str_name = get_string(str_message)
            str_message = 'Введите фамилию контакта: '
            str_family = get_string(str_message)
            str_message = 'Введите дату рождения: '
            str_birth_date = get_string(str_message)
            str_message = 'Введите место работы: '
            str_organization = get_string(str_message)
            return [2, [int_phone, str_name, str_family, str_birth_date, str_organization]]
        case 2:
            return get_main_menu()


def import_menu():
    while True:
        str_message ='Введите:\n\
            1 - для импорта данных из CSV\n\
            2 - для импорта данных из HTML\n\
            3 - для возврата в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 3, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            return [3, 1]
        case 2:
            return [3, 2]
        case 3:
            return get_main_menu()

def export_menu():
    while True:
        str_message ='Введите:\n\
            1 - для экспорта справочника в CSV\n\
            2 - для экспорта справочника в HTML\n\
            3 - для возврата в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 3, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            return [4, 1]
        case 2:
            return [4, 2]
        case 3:
            return get_main_menu()


def drop_menu():
    while True:
        str_message ='Вы уверены, что хотите стереть справочник? Все данные будут потеряны.\n\
            1 - стереть данные справочника\n\
            2 - вернуться в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 2, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            return [5]
        case 2:
            return get_main_menu()


def exit_menu():
    while True:
        str_message ='Вы уверены, что хотите прекратить работу со справочником?\n\
            1 - да, прекратить работу со справочником\n\
            2 - нет, вернуться в главное меню\n\
            Ваш выбор: '
        int_answer = get_natural_number(str_message, 2, 1)
        if int_answer is None: print('Неверный ввод данных. Введите число.')
        else: break
    match int_answer:
        case 1:
            return [6]
        case 2:
            return get_main_menu()


def get_natural_number(str_message, int_max, int_min = 1):
    try:
        number = float(input(str_message))
        if number % 1 == 0 and number >= int_min and number <= int_max:
            return int(number)
        else:
            return None
    except:
        return None


def get_string(str_message):
    return input(str_message)


def get_phone_number(str_message):
    while True:
        try:
            str_number = input(str_message)
            if len(str_number) != 11: print(str_message)
            else:
                number_phone = ''
                for number in str_number:
                    if int(number) % 1 == 0:
                        number_phone += number
                    else:
                        print(str_message)
                        break
                return number_phone
        except:
            print(str_message)
