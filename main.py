#!/usr/bin/env python3

from gears import getToken, autoCheckIn, sendMessage
import requests


postUrl = 'https://candidature.1337.ma/users/sign_in'


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

while True:
    s = login(postUrl)
    check = s.get('https://candidature.1337.ma/meetings')

    results = autoCheckIn(check.content)
 
    if (results != '#'):
        break

# Send The SMS to me

tb = sendMessage()
print(tb)

