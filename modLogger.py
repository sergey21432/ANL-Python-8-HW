from datetime import datetime as dt

def write_log(strAction = ''):
    strTime = dt.now().strftime('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write(f'{strTime};{strAction}\n')


