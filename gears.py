from bs4 import BeautifulSoup
from lxml import html
import requests
import creds


def getToken(req):
    soup = BeautifulSoup(req, 'html.parser')
    token = soup.find("meta", {"name": "csrf-token"}).attrs['content']

    if (token == None):
        return ('[!] An error happend while extracting the token.')
    else:
        return (token)


def autoCheckIn(data):
    #Xpath: '//*[@id="subs-banner"]/nav/ul/li[6]/a'

    parsed = html.fromstring(data)
    result = parsed.xpath('//*[@id="subs-banner"]/nav/ul/li[5]/a')
    return(result[0].attrib['href'])


def sendMessage():
    resp = requests.post('https://textbelt.com/text', {
        'phone': creds.TARGET,
        'message': creds.MESSAGE,
        'key': 'textbelt',
    })
    return(resp.json())
