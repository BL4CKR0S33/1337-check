#!/usr/bin/env python3

from gears import getToken, autoCheckIn, sendMessage, addReport, sendReport
from datetime import *
import requests
import schedule
import time





postUrl = 'https://candidature.1337.ma/users/sign_in'

date = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
sdate = f'{date.day}/{date.month} - {date.hour}:{date.minute}'

attempts = 0

print(f'[{sdate}] [+] App started successfully.\n')
print('-----------------------------------------\n')

def login(url):
    session = requests.Session()

    # Get the token from the meta tag
    req = session.get(url)
    token = getToken(req.text)

    payload = {
        'utf8': "✓",
        'authenticity_token': token,
        'user[email]': "abdelghanibraimi@outlook.com",
        'user[password]': "Tffw2z&Q/!MT&a?",
        'commit': "Sign+in"
    }

    res = session.post(url, data=payload)
    return (session)


def main():
    global attempts, postUrl, sdate

    s = login(postUrl)
    check = s.get('https://candidature.1337.ma/meetings')

    results = autoCheckIn(check.content)
    
    attempts += 1

    if (results != '#'):
        data = f'[CONGRATULATIONS]\n[{sdate}][!] [Try number {attempts}] [Succeded]'
        sendMessage(data)
        print('\n[+] App ended successfully.\n')
        exit()
    else:
        data = f'[{sdate}][!] [Try number {attempts}] [Failed]\n'
        print(data)
        
        addReport(data)
    s.close()

schedule.every(6).hours.do(main)
schedule.every(24).hours.do(sendReport)

while True:
    schedule.run_pending()
    time.sleep(1)








