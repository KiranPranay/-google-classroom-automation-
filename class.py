import sys
from time import sleep
from classes_today import *
from quotes import print_random_quote
from config import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
inp = sys.argv[1].upper()

if inp in classes:
    open_link(classes[inp])
elif inp == 'TODAY' or inp == '-T':
    print()
    print_random_quote()
    classes_today()
elif inp == 'HELP' or inp == '-H':
    help_menu()
elif inp == 'AUTOMATE' or inp == '-A':
    subs = find_classes()
    c = 0
    while True:
        if c == 1:
            break
        time = datetime.now().time()
        time = str(time).split(':')
        for i in subs:
            if time[0] == i[0:2] and time[1] == i[3:5] and 'LUNCH' not in i:
                # open_link(classes[i[20:]])
                #Loads chrome with default settings
                opt=Options()
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.geolocation": 1,
                "profile.default_content_setting_values.notifications": 1
                })
                #Gives path to chrome webdriver and loads classroom webpage
                driver=webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\ChromeDriver/chromedriver.exe')
                required_meet_link = classes[i[20:]]
                required_link = 'https://accounts.google.com/signin/v2/identifier?continue='+required_meet_link+'&sacu=1&hl=en_US&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
                driver.get(required_link)
                print('Opened ' + i[20:] + ' link')
                #Logs in the classroom
                username=driver.find_element_by_id('identifierId')
                username.click()
                username.send_keys(config['user'])
                next=driver.find_element_by_class_name('VfPpkd-vQzf8d')

                next.click()
                sleep(2)
                password=driver.find_element_by_name('password')
                password.click()
                password.send_keys(config['pass'])

                next=driver.find_element_by_class_name('VfPpkd-vQzf8d')
                next.click()
                #Do not worry, intentionally delayed for 15sec
                sleep(15)

                #Turns off mic and camera and joins the meet
                # camera=driver.find_elements_by_class_name('I5fjHe wb61gb')
                # camera.click()

                # mic=driver.find_element_by_class_name('I5fjHe wb61gb')
                # mic.click()

                #joining the meet
                join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
                join.click()
                
                if i == subs[-1]:
                    c = 1
                    break
                sleep(3600)
                break

else:
    print('\n' + '\t' + 'Invalid command')
    print('\n' + '\t' + 'Try class -h for help menu')
