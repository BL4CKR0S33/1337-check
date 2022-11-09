#!/usr/bin/env python3

from gears import getToken, autoCheckIn, sendMessage, addReport, generalReport
from datetime import *
import requests
import schedule
import time

postUrl = 'https://candidature.1337.ma/users/sign_in'

date = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
sdate = f'{date.day}/{date.month} - {date.hour}:{date.minute}'

attempts = 0

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
    print('[!] Try number: {} - Failed.'.format(str(attempts)))
    


    if (results == '#'):
        data = f'[{sdate}][!] [Try number {attempts}] [Failed]'
        sendMessage(data)
    
    s.close()

#schedule.every(6).hours.do(main)
schedule.every(7).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)








