from modDB import get_data as gd


def create_HTML():
    style = 'style="font-size:22px"'
    html = '<html>\n <head>Телефонный справочник</head>\n <body>\n'
    for lst_contact in gd():
        html += f'<p {style}> Telephone: {lst_contact[0]} </p>\n'
        html += f'<p {style}> Name: {lst_contact[1]} </p>\n'
        html += f'<p {style}> Family: {lst_contact[2]} </p>\n'
        html += f'<p {style}> Birth day: {lst_contact[3]} </p>\n'
        html += f'<p {style}> Organization: {lst_contact[4]} </p>\n'
        html += '<p><br></p>\n'
    with open('expHTML.html', 'w') as page:
        page.write(html)


def create_CSV():
    with open ('expCSV.csv', 'w') as file:
        for lst_contact in gd():
            strContact = ''
            for str_info in lst_contact:
                strContact += f'{str_info};'
            file.writelines(strContact[:-1] + '\n')
