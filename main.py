#!/usr/bin/env python3

from gears import getToken, autoCheckIn, sendMessage, addReport, sendReport
from creds import SCHOOL_EMAIL, SCHOOL_PASSWORD
from datetime import *
import requests
import schedule
import time





postUrl = 'https://candidature.1337.ma/users/sign_in'

date = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
sdate = f'{date.day}/{date.month} - {date.hour}:{date.minute}'

attempts = 0

proxies = { 
              "http"  : "http://203.30.189.253:80", 
              "http"  : "http://203.34.28.117:80", 
              "http"  : "http://173.245.49.102:80", 
              "http"  : "http://203.23.106.138:80", 
              "http"  : "http://45.14.174.73:80", 
              "http"  : "http://203.24.103.252:80", 
              "http"  : "http://23.227.38.26:80", 
              "http"  : "http://203.23.103.138:80", 
              "http"  : "http://203.13.32.182:80", 
              "http"  : "http://203.30.190.114:80", 
              "http"  : "http://203.24.108.211:80", 
              "http"  : "http://188.114.98.153:80", 
              "http"  : "http://103.21.244.99:80", 
              "http"  : "http://188.114.99.234:80", 
              "http"  : "http://45.8.105.89:80", 
              "http"  : "http://203.32.120.182:80", 
              "http"  : "http://203.30.189.94:80", 
              "http"  : "http://185.162.231.49:80", 
              "http"  : "http://203.24.102.82:80", 
              "http"  : "http://203.24.103.85:80" 
}

print(f'[{sdate}] [+] App started successfully.\n')
print('-----------------------------------------\n')

def login(url, proxies):
    session = requests.Session()

    # Get the token from the meta tag
    req = session.get(url)
    token = getToken(req.text)

    payload = {
        'utf8': "✓",
        'authenticity_token': token,
        'user[email]': SCHOOL_EMAIL,
        'user[password]': SCHOOL_PASSWORD,
        'commit': "Sign+in"
    }

    res = session.post(url, data=payload, proxies=proxies)
    return (session)


def main():
    global attempts, postUrl, sdate

    s = login(postUrl, proxies)
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

# schedule.every(6).hours.do(main)
while True:
        main(proxies)

schedule.every(24).hours.do(sendReport)

while True:
    schedule.run_pending()
    time.sleep(1)








