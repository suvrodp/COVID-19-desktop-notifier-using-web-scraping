import schedule
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from win10toast import ToastNotifier

def notifier():
    site= "https://www.worldometers.info/coronavirus/country/india/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    tags=soup('li', {"class":"news_li"})
    new_cases=tags[0].strong.text.split()[0]
    new_death=list(tags[0].strong.next_siblings)[1].text.split()[0]


    noti=ToastNotifier()
    message= "New cases: "+new_cases+"\nNew deaths: "+new_death
    noti.show_toast(title="COVID19 Update", msg=message,duration=10, icon_path="corona_corona_virus_coronavirus_disease_epidemic_icon_141517.ico")


notifier()