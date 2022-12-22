import modDB as DB
import modExport as ET
import modImport as IT
import modLogger as LG
import modUI as UI

while True:
    LG.write_log('Start program')
    lst_answer = UI.get_main_menu()
    match lst_answer[0]:
        case 1:
            lst_data = DB.get_contact(lst_answer[1], lst_answer[2])
            if len(lst_data) == 0:
                print('Контакт не найден в телефонной книге')
                LG.write_log('Error get contact: ' + lst_answer[1] + ' ' + lst_answer[2] + '.')
            else:
                print(*DB.get_contact(lst_answer[1], lst_answer[2]))
                LG.write_log('Get contact ' + lst_answer[1] + ' ' + lst_answer[2] + '.')

        case 2:
            DB.write_contact([lst_answer[1]])
            LG.write_log('Add contact ' + lst_answer[1][2] + ': '+ lst_answer[1][0] + '.')
            print('Контакт добавлен.')
        case 3:
            match lst_answer[1]:
                case 1:
                    IT.import_CSV()
                    LG.write_log('Import from .csv')
                    print('Импорт закончен.')
                case 2:
                    IT.import_HTML()
                    LG.write_log('Import from .html')
                    print('Импорт закончен.')
        case 4:
            match lst_answer[1]:
                case 1:
                    ET.create_CSV()
                    LG.write_log('Export in .csv')
                    print('Экспорт закончен.')
                case 2:
                    ET.create_HTML()
                    LG.write_log('Export in .html')
                    print('Экспорт закончен.')
        case 5:
            DB.drop()
            LG.write_log('Drop telephone book')
            print('Телефонная книга очищена.')
        case 6:
            LG.write_log('Exit program')
            print('Выход из программы.')
            break
