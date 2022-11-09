from bs4 import BeautifulSoup
from lxml import html
from twilio.rest import Client
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
    result = parsed.xpath('//*[@id="subs-banner"]/nav/ul/li[6]/a')
    return(result[0].attrib['href'])


def sendMessage(body):
    client = Client(creds.ACCOUNT_SID, creds.AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=creds.SENDER,
        to=creds.TARGET,
    )


def addReport(data):
    with open("./reports/report.txt", "a") as f:
        f.write(data)


def sendReport():
    with open("./reports/report.txt", "r") as f:
        report = f.read()
    if (report):
        sendMessage(report)
        with open('./reports/report.txt', 'w') as d:
            d.write('')
    else:
        return('[!] There is a problem located in gears.py;line:39>47')








