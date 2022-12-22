from modDB import write_contact as wc


def import_HTML():
    with open('impHTML.html', 'r') as page:
        data = [[x[x.find(':', x.find('>')) + 2: x.find('</p>') - 1] for x in strContact.splitlines() if ':' in x] for strContact in page.read().split('<p><br></p>\n')]
        wc(data[:-1])


def import_CSV():
    with open('impCSV.csv', 'r') as file:
            data = [strContact.split(';') for strContact in file.read().splitlines()]
            wc(data)
