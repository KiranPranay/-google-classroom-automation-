import calendar
from datetime import datetime
import webbrowser

subjects = {'monday' : ['FFEM', 'CAD-CAM', 'NT'],
                'tuesday' : ['HT', 'NT', 'R&AC'],
                'wednesday' : ['FFEM', 'NT', 'HT-LAB'],
                'thursday' : ['FFEM', 'HT', 'COI'],
                'friday' : ['CAD-CAM', 'R&AC', 'HT'],
                'saturday' : ['CAM-LAB', 'CAM-LAB', 'AECS_LAB']
              }
classes = { 'HT':	'https://meet.google.com/mcd-echr-pfy',
            'NT' : 'https://meet.google.com/vzo-gevy-dtn',
            'CAD-CAM' : 'https://meet.google.com/gsb-dkos-zsv',
            'FFEM' : 'https://meet.google.com/kkt-czwj-aog',
            'R&AC' :'https://meet.google.com/ngf-ceoy-yeb',
            'HT-LAB' : 'https://meet.google.com/ngf-ceoy-yeb',
            'CAM-LAB' : 'https://meet.google.com/awi-eypk-zdc',
            'AECS_LAB' : 'https://meet.google.com/ngf-ceoy-yeb',
            'COI' : 'https://meet.google.com/ngf-ceoy-yeb'
          }

def find_day():
    date_and_time = datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[date]
    return day.lower()

def find_classes():
    subs = []
    day = find_day()
    classes = subjects[day]
    if day != 'sunday':
        timings = ['09:40 am - 10:40 am','10:50 am - 11:50 am', '12:00 pm - 13:00 pm']
        for i in range(3):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    if day == 'sunday':
        timings = ['09:40 am - 10:40 am','10:50 am - 11:50 am', '12:00 pm - 13:00 pm']
        for i in range(3):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    return subs

def classes_today():
    subs = find_classes()
    for i in subs:
        time = datetime.now().time()
        time = str(time).split(":")
        if time[0] == i[0:2] and time[1] >= i[3:5]:
            print('\n' + '\t' + i,' <-- Present Session')
        elif time[0] == i[11:13] and time[1] < i[14:16]:
            print('\n' + '\t' + i,' <-- Present Session')
        else:
            print('\n' + '\t' + i)

def help_menu():
    print('\n\t --->>> AUTOMATING GOOGLE CLASSROOM V 1.0 <<<---')
    print('\n\t COMMAND                  DESCRIPTION')
    print('\n\t class [-a or automate]   To automate')
    print('\n\t class [-h or help]       To see this menu')
    print('\n\t class [subject_name]     To open subject_name\'s link')
    print('\n\t class [-t or today]      To see today\'s classes')

def open_link(url):
    webbrowser.open(url)
    print('opened requested page')
