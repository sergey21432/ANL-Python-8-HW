def write_contact(lst_Data):
    with open('DB.txt', 'a') as file:
        for lst_Contact in lst_Data:
            for x in lst_Contact:
                file.writelines(x + '\n')
            file.writelines(':::\n')


def get_data():
    with open('DB.txt', 'r') as file:
        data = [[x for x in strContact.splitlines()] for strContact in file.read().split(':::\n')]
        return data[:-1]


def get_contact(strFamily, strName = ''):
    return [x for x in get_data() if (strName == x[1] or strName == '') and strFamily == x[2]]


def drop():
    with open('DB.txt', 'w') as file:
        file.truncate()
